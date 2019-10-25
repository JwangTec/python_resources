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


# tcp和ip协议
class WebServer:
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 重启的时候 不用去改端口号
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip地址和端口号
        self.ss.bind(('10.2.0.104', 25535))
        self.ss.listen(10)
        self.sql = {}

    def run(self):

        while 1:
            conn, addr = self.ss.accept()
            msg = conn.recv(65535)
            url = self.get_url(msg)
            xx = self.cokie(msg)
            print(xx)
            arguments = self.get_argument(msg)
            func = self.url_header(url)
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n" \
                              "Connection: Closed\r\nSet-Cookie: xx=qwqweqeqeqeqe\r\n\r\n"
            try:
                response_body = func(arguments)
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

        response_body = self.render(response_body,'未登陆用户')
        return response_body

    def p1904(self, arguments):
        with open('test2.html', 'r') as f:
            response_body = f.read()
            return response_body

    def register(self, arguments):
        with open('reg.html', 'r') as f:
            response_body = f.read()
            return response_body

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
            cursor.close()
            sql_conn.commit()
            sql_conn.close()
        if count >= 1:
            name = username

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

    def cokie(self,msg):
        msg = msg.decode()
        msg_list = msg.split('\r\n')
        argument_cokie = dict()
        try:
            argument_str = msg_list
        except IndexError:
            return
        for i in argument_str:
            if 'Cookie' in i:
                list1 = i.split(' ')
                list2 = list1[1]
                list2 = list2.split('=')
                argument_cokie[list2[0]] = list2[1]
        return argument_cokie


    def if_sql_cokie(self,msg):
        argument_cokie = self.cokie(msg)
        sql_conn = self.mysql_conn()
        count = 0

        if argument_cokie is not None:
            key = argument_cokie.keys()
            value = argument_cokie.values()
            sql = "select * from (select * from web_1 join sension_web on web_1.id = sension_web.web_1id) a where a.key={} and a.value={}".format(key,value)
            cursor = sql_conn.cursor()
            count = cursor.execute(sql)
            cursor.close()
            sql_conn.commit()
            sql_conn.close()
        if count >= 1:
            print('--------------------')

    def url_header(self, url):
        print(url)
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
            database="web_ser",
            charset='utf8')
        return conn


if __name__ == '__main__':
    s = WebServer()
    s.run()
