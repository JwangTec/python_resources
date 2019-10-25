'''
简易web服务器
0.设置服务器
1.接收tcp/ip协议
2.接收http报文
3.编写响应报文头+一行空格+html代码
4.发送响应报文
'''

import socket
import re
import pymysql


# 0

class ServerWeb:
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ss.bind(('10.2.0.104', 8809))
        self.ss.listen(10)

    def run(self):
        while 1:
            # 1
            conn, addr = self.ss.accept()
            # 2
            msg = conn.recv(1024)

            url = self.get_url(msg)
            arguments = self.get_argument(msg)
            func = self.url_header(url)
            print(arguments)
            response_header = "HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\nTransfer-Encoding: chunked" \
                                  "Connection: Closed\r\n\r\n"
            try:
                body = func(arguments)
                conn.send((response_header+body).encode())
                conn.close()
            except Exception:
                pass


    def user_get(self):
        pa = r'\r\n\r\n*'

    def mysql_conn(self):
        conn = pymysql.connect(
            host='localhost',
            user='root', password='wang1995',
            database='webdb',
            charset='utf8')

        return conn

    def sql_select(self,arguments):
        print(arguments)
        mysql_conn = self.mysql_conn()
        if arguments is not None:
            username = arguments['username']
            password = arguments['passworld']
            cursor = mysql_conn.cursor()
            sql = "select * from load_user where username = '{}' and password = '{}'".format(username,password)
            res = cursor.execute(sql)
            mysql_conn.commit()
            mysql_conn.close()
            return res

    def sql_insert(self,arguments):
        mysql_conn = self.mysql_conn()
        cursor = mysql_conn.cursor()
        sql = "insert into load_user(`username`,`password`) value ('{}','{}')".format(user,paw)
        cursor.execute(sql)
        mysql_conn.commit()
        mysql_conn.close()


    def get_url(self, msg):
        msg_list = msg.split()
        return msg_list[1]

    def url_header(self, url):
        #首页
        if url == b'/':
            return self.index
        #注册
        if url == b'/register':
            return self.register

    def index(self):
        with open('index.html', 'r') as r:
            x = r.read()
        return x

    def register(self):
        with open('reg.html', 'r') as r:
            x = r.read()
        return x





    def get_argument(self,msg):
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
                key,value = tuple(argument.split('='))
                argument_dict[key] = value
            except Exception:
                return argument_dict

        return argument_dict




if __name__ == '__main__':
    s = ServerWeb()
    s.run()

# xx = msg.decode()
# pa = 'GET /* HTTP/1.1\r\n'
# x = re.findall(pa,xx)
#
# if len(x) == 0:
#
# #3
#     response_header = "HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\nTransfer-Encoding: chunked" \
#                   "Connection: Closed\r\n\r\n<html><head><mata charset='UTF-8'><head>" \
#                   "<body><div>阿萨大帝</div></body></html>"
# #4
#     conn.send(response_header.encode())
#
# else:
#     # 3
#     response_header = "HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\nTransfer-Encoding: chunked" \
#                       "Connection: Closed\r\n\r\n<html><head><mata charset='UTF-8'><head>" \
#                       "<body><div>xxxxxxx</div></body></html>"
#     # 4
#     conn.send(response_header.encode())
# print(msg)

'''

1.识别网址 并返回不同页面
2.可加载外部的web文件
3.服务器与数据库的链接
4.注册：插入数据到数据库
5.登陆：查询数据在数据库中是否匹配
6.登陆保持：cookie/session
'''