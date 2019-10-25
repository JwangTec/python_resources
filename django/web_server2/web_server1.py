"""
http协议 --> 应用层协议
浏览器会默认的加上80端口号

# 1. 识别不同的网址 --> 返回不同的页面
# 2. 能够加载外部的html文件进来
# 3. 服务器去链接数据库
# 4. 注册功能 --> 插入一条数据到mysql中
# 5. 登陆功能 --> 在数据库中查询 在注册的时候插入的账户密码是否匹配
# 6. 保持登陆 --> cookie 或者 session
"""
import socket
import pymysql
import uuid
from datetime import datetime,timedelta

# tcp和ip协议
class WebServer:
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 重启的时候 不用去改端口号
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip地址和端口号
        self.ss.bind(('10.2.0.104', 10082))
        self.ss.listen(10)
        self.session_id =None

    def get_time(self,days=5):
        return datetime.now() + timedelta(days=days)

    def run(self):
        while 1:
            conn, addr = self.ss.accept()
            msg = conn.recv(65535)
            url = self.get_url(msg)
            print(msg)
            arguments = self.get_argument(msg)
            func = self.url_header(url)
            try:
                response_body = func(arguments)
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n" \
                                  "Connection: Closed\r\nSet-Cookie: session_id={}\r\n\r\n".format(self.session_id)
                conn.send((response_header + response_body).encode())
                conn.close()
            except Exception:
                pass

    def render(self,data, replace):
        """
        渲染技术
        :param data:
        :param replace:
        :return:
        """
        import re
        pattern = re.compile('{{ }}')
        res = re.sub(pattern, replace, data)
        return res

    def index(self, arguments):
        with open('index.html', 'r') as f:
            response_body = f.read()
        session_id = arguments['session_id']
        mysql_conn = self.mysql_conn()
        cursor = mysql_conn.cursor()
        sql = "select web_1.username from sension_web join web_1 on sension_web.web_1id=web_1.id where sension_web.serect_key='{}'".format(session_id)
        cursor.execute(sql)
        res = cursor.fetchone()
        mysql_conn.commit()
        cursor.close()
        mysql_conn.close()
        if res is not None:
            name = res[0]
        else:
            name = '未登陆用户'
        response_body = self.render(response_body,name)
        self.session_id = session_id
        return response_body

    def p1904(self, arguments):
        with open('test2.html', 'r') as f:
            response_body = f.read()
            return response_body

    def register(self, arguments):
        with open('reg.html', 'r') as f:
            response_body = f.read()
            return response_body

    def gen_uuid(self):
        """
        生成一个随机码作为session
        :return:
        """
        return uuid.uuid4().hex

    def login1(self, arguments):
        sql_conn = self.mysql_conn()
        count = 0
        name = '未登陆用户'
        if arguments is not None:
            username = arguments['username']
            password = arguments['password']
            sql = "select * from web_1 where `username`='{}' and `password`='{}'".format(username, password)
            cursor = sql_conn.cursor()
            count = cursor.execute(sql)
            data = cursor.fetchone()
            cursor.close()
            sql_conn.commit()

        if count >= 1:

            name = username
            session_id = self.gen_uuid()
            sql = "insert into `sension_web` (`key`,`datetime`,`web_1id`)" \
                  "values ('{}','{}','{}')".format(session_id,self.get_time(),data[0])
            self.session_id = session_id
            cursor = sql_conn.cursor()
            count = cursor.execute(sql)
            cursor.close()
            sql_conn.commit()
        sql_conn.close()
        with open('index.html', 'r') as f:
            response_body = f.read()
        response_body = self.render(response_body, name)
        return response_body

    def register1(self, arguments):
        sql_conn = self.mysql_conn()
        if arguments is not None:
            username = arguments['username']
            password = arguments['password']
            sql = "insert into `web_1` (`username`,`password`) values ('{}','{}')".format(username, password)

            cursor = sql_conn.cursor()
            cursor.execute(sql)
            sql_conn.commit()
            sql_conn.close()

        with open('index.html', 'r') as f:
            response_body = f.read()
            return response_body

    def login(self, arg):
        with open('login.html', 'r') as f:
            response_body = f.read()
            return response_body

    def get_argument(self, msg):
        """
        专门获取参数
        :param msg:
        :return:
        username=asdf&pwd=asdf&repwd=sadf

        [username=asdf,pwd=asdf,repwd=sadf]
        """
        msg = msg.decode()
        msg_list = msg.split('\r\n\r\n')
        argument_dict = dict()

        session_id=self.get_session_id(msg)
        argument_dict['session_id'] = session_id
        try:
            argument_str = msg_list[1]
        except IndexError:
            return argument_dict

        if '&' not in argument_str:
            argument_str += '&'
        argument_list = argument_str.split('&')
        for argument in argument_list:
            try:
                key, value = tuple(argument.split('='))
                argument_dict[key] = value
            except Exception:
                return argument_dict


        return argument_dict

    def get_session_id(self,string):
        msg_list = string.split('\r\n')
        for msg in msg_list:
            if msg.startswith('Cookie:'):
                cookies = msg[len("Cookie:"):len(string)-1]
                cookie_list = cookies.split(';')
                for cookie in cookie_list:
                    cookie = cookie.replace(' ', "")
                    if cookie.startswith('session_id='):
                        serect_key = cookie.split('=')[-1]
                        return serect_key
                break
        return None

    def url_header(self, url):
        if url == b'/':
            return self.index
        if url == b'/p1904':
            return self.p1904
        if url == b'/login':
            return self.login
        if url == b'/login1':
            return self.login1
        if url == b'/register':
            return self.register
        if url == b'/register1':
            return self.register1
        return '404.html'

    def get_url(self, msg):
        msg_list = msg.split()
        return msg_list[1]

    def mysql_conn(self):
        conn = pymysql.connect(
            host='localhost',
            user='root', password='wang1995',
            database='web_ser',
            charset='utf8')
        return conn


if __name__ == '__main__':
    s = WebServer()
    s.run()
