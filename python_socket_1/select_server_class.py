import select
import socket

class Server:
    def __init__(self,host_ip='10.2.0.104',port=25535,listen_num = 10):
        self.ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ss.bind((host_ip,port))
        self.ss.listen(listen_num)
        self.read_list = []
        self.write_list = []
        self.host_ip = host_ip
        self.port = port
        self.listen_num = listen_num
        self.error_list = []
        self.recv_msg = {}

    def remove_conn(self,conn):
        self.remove_read(conn)
        self.remove_write(conn)

    def remove_read(self,conn):
        try:
            self.read_list.remove(conn)
        except Exception:
            pass

    def remove_write(self,conn):
        try:
            self.write_list.remove(conn)
        except Exception:
            pass






    def run(self):
        print("本地服务器启动 IP：{} 端口号：{} 最大链接数：{}".format(self.host_ip,self.port,self.listen_num))
        while True:
            rlist,wlist,xlist = select.select(self.read_list,self.write_list,self.error_list)
            for r in rlist:
                if r == self.ss:
                    try:
                        conn, addr = self.ss.accept()
                    except Exception as a:
                        print('服务器出现错误：{}'.format(a))
                        return
                    if conn not in self.read_list:
                        self.read_list.append(conn)
                        print("用户{}已连接到服务器".format(conn.fileno()))
                else:
                    msg = b''
                    while True:
                        tmp_msg = r.recv(1)
                        if tmp_msg == '@#':
                            print('消息接收完毕\n')
                            break
                        msg += tmp_msg
                    if len(msg) == 0:
                        try:
                            r.close()
                        except Exception:
                            pass

                        self.remove_conn(r)
                        continue

                    res_msg = '账号：{}\n信息内容{}'.format(r.fileno(), msg.encode())
                    print(res_msg)

                    for conn in self.read_list:
                        if conn is not self.ss:
                            if conn is not self.write_list:
                                self.write_list.append(conn)
                                self.recv_msg[conn] = res_msg

            for w in wlist:
                msg = self.recv_msg.get(w, None)
                if msg is None:
                    continue
                try:
                    w.send(msg)
                except Exception:
                    self.remove_conn(w)
                    continue
                self.remove_write(w)


if __name__ == "__main__":
    s = Server()
    s.run()



