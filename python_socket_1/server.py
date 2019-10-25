import socket
import threading
#socket.AF_INET --> ip,ip6
# socket.SOCK_STREAM  --> tcp,udp
#ss是一个对象 bind函数 在什么ip地址和什么端口运行这个程序
# listen 表示我们是一个服务端程序
# c/s模式    client 和 server分离模式
# 单机游戏

class Server:
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ss.bind(('10.2.0.26',19528))
        #最大能监听10个人同时进来 还表示这个是一个聊天的服务端
        self.ss.listen(10)
        print('服务已经启动')

        self.conn_list = []


    def recv_msg(self,conn):
        while True:
            try:
                msg = conn.recv(100000)
            except Exception:
                self.conn_list.remove(conn)
                conn.close()
                return
            if len(msg) == 0:
                print('客户端已经断开链接')
                self.conn_list.remove(conn)
                conn.close()
                return
            print('{}链接说{}'.format(str(conn.fileno()),msg.decode()))
            for c in self.conn_list:
                try:
                    c.send('已收到{}发送的消息:{}'.format(str(conn.fileno()),msg.decode()).encode())
                except Exception:
                    self.conn_list.remove(conn)
                    conn.close()

    def run(self):
        #等待链接进来 conn表示的是会话
        while True:
            #如果有阻塞 踢出去  | 执行的代码过多也会踢出去
            try:
                conn,addr = self.ss.accept()  #被动接收客户端信息，会形成阻塞
            except Exception:
                print('服务程序出错 停止运行')
                break
            self.conn_list.append(conn)
            print('有新的链接进来 {}'.format(conn))
            print('当前通信使用的线路是{}'.format(conn.fileno()))
            #接受消息 发送消息 一次性的能接受多少B消息  msg 是一个utf8编码后的
            # recv_msg(conn,test)
            task = threading.Thread(target=self.recv_msg,args=(conn,))  #相当于去掉该函数里的 while的阻塞
            task.start()

if __name__ == "__main__":
    s = Server()
    s.run()


