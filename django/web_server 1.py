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
        self.ss.bind(('10.2.0.26', 10080))
        self.ss.listen(10)

    def run(self):
        while 1:
            print('aaaaaa')
            conn, addr = self.ss.accept()
            msg = conn.recv(65535)
            print(msg)
            url = self.get_url(msg)
            func = self.url_header(url)
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n" \
                          "Connection: Closed\r\n\r\n"
            try:
                response_body = func()
                conn.send((response_header + response_body).encode())
                conn.close()
            except Exception:
                pass

    def index(self):
        with open('index.html', 'r') as f:
            response_body = f.read()
            return response_body
    def p1904(self):
        with open('test2.html', 'r') as f:
            response_body = f.read()
            return response_body

    def register(self):
        with open('reg.html', 'r') as f:
            response_body = f.read()
            return response_body



    def url_header(self, url):
        print(url)
        if url == b'/':
            return self.index
        if url == b'/p1904':
            return self.p1904

        if url == b'/login':
            return self.login

        if url == b'/register':
            return self.register
        return '404.html'

    def get_url(self, msg):
        msg_list = msg.split()
        return msg_list[1]

    def mysql_conn(self):
        conn = pymysql.connect(
            host='10.2.0.26',
            user='p1904', password='p1904_123',
            database='my_web',
            charset='utf8')

        return conn


if __name__ == '__main__':
    s = WebServer()
    s.run()
