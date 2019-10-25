from select import poll,select,kqueue,POLLIN,POLLOUT
import socket
p = poll()
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('10.2.0.26', 9527))
ss.listen(10)
p.register(ss.fileno(),POLLIN)
conn_table = {}
msg_dict ={}
while True:
    events = p.poll() # 如果timeout为None，将会阻塞，知道有事件发生
    #events --->[(ss.fileno(),POLLIN),(conn,POLLOUT)]
    for event in events:
        fileno,fd = event
        if fileno == ss.fileno():
            conn,addr = ss.accept()
            p.register(conn.fileno(),POLLIN)
            conn_table[conn.fileno()] = conn
        else:
            conn = conn_table[fileno]
            if fd == POLLIN:
                msg = conn.recv(65535)
                res_msg = "编号为{}的用户说{}".format(str(fileno),msg.decode()).encode()
                #注册写事件
                for conn in conn_table.values():
                    p.register(conn.fileno(),POLLOUT)
                    msg_dict[conn.fileno()] = res_msg
            elif fd == POLLOUT:
                msg = msg_dict[fileno]
                conn.send(msg)
                p.unregister(fileno)
                p.register(fileno,POLLIN)


