import socket
import threading

class Server:
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind(('10.2.0.104', 19530))  # 相当于总服务器
        self.ss.listen(10)
        print('start runing')

        self.conn_num = []

    def recv_msg(self,conn):
        while True:
            try:
                msg = conn.recv(1024)
            except Exception:
                self.conn_num.remove(conn)
                conn.close()
                return
            if len(msg) == 0:
                print('账号：{}  已经断开链接'.format(conn.fileno()))
                self.conn_num.remove(conn)
                conn.close()
                return
            print('账号为：{}\r信息内容：{}\n'.format(str(conn.fileno()),msg.decode()))


            for c in self.conn_num:
                try:
                    c.send('\n来自账号：{}\r信息内容:{}\n'.format(str(conn.fileno()),msg.decode()).encode())
                except Exception:
                    self.conn_num.remove(conn)
                    conn.close()

    def run(self):
        while True:
            # 如果有阻塞 踢出去  | 执行的代码过多也会踢出去
            try:
                conn, addr = self.ss.accept()
            except Exception:
                print('服务程序出错 停止运行')
                break
            self.conn_num.append(conn)
            print('有新的链接进来 {}\n'.format(conn))
            # 接受消息 发送消息 一次性的能接受多少B消息  msg 是一个utf8编码后的
            # recv_msg(conn,test)
            task = threading.Thread(target=self.recv_msg, args=(conn,))
            task.start()

if __name__ == "__main__":
        s = Server()
        s.run()



