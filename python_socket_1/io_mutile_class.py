import select
import socket

class Server:
    def __init__(self,host_ip='10.2.0.26',port=19528,listen_num=10):
        self.port = port
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ss.bind((host_ip, self.port))
        self.ss.listen(listen_num)
        self.read_list = [self.ss]
        self.write_list = []
        self.error_list = []
        self.msg_dict = {}

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
        print('服务程序已经开启,当前服务程序的端口号为{}'.format(str(self.port)))
        while True:
            rlist,wlist,xlist = select.select(self.read_list,self.write_list,self.error_list,timeout=1)
            for r in rlist:
                if r is self.ss:
                    try:
                        conn,addr = self.ss.accept()
                    except Exception as e:
                        print('服务器错误 终止服务{}'.format(e))
                        return

                    if conn not in self.read_list:
                        self.read_list.append(conn)
                        print('新链接进来')

                else:
                    msg = r.recv(1024)
                    if len(msg) == 0:
                        try:
                            r.close()
                        except Exception:
                            pass
                        self.remove_conn(r)
                        continue

                    res_msg = "昵称为**{}**说:{}".format(str(r.fileno()), msg.decode()).encode()
                    print(res_msg)
                    for conn in self.read_list:
                        if conn is not self.ss:
                            if conn not in self.write_list:
                                self.write_list.append(conn)
                                self.msg_dict[conn] = res_msg

            for w in wlist:
                msg = self.msg_dict.get(w,None)
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



