'''
qq群聊聊天室
'''

from select import poll,select,kqueue,POLLIN,POLLOUT
import socket

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #重启服务器不需要改变端口号
ss.bind(('10.2.0.104',12306))

ss.listen(10)

p = poll()
print('qq群聊服务器启动--')
p.register(ss.fileno(),POLLIN)

conn_table = {}
msg_recv = {}
while True:
    events = p.poll()

    for event in events:
        fileno,fd = event

        if fileno == ss.fileno():
            conn,addr = ss.accept()
            print('账号：{} 已加入群聊\n-----------------------'.format(conn.fileno()))
            p.register(conn.fileno(),POLLIN)
            conn_table[conn.fileno()] = conn


        else:
            conn = conn_table[fileno]
            if fd == POLLIN:
                msg = conn.recv(1024)
                msg = msg.decode()
                str1 = '@'
                index_1 = msg.index(str1)
                xx = msg[:index_1]
                yy = msg[index_1+1:]
                res_msg = '账号：{} \n昵称：{}\n信息内容：{}'.format(conn.fileno(),yy,xx).encode()
                print('账号: {}\n信息: {}\n----------------------'.format(conn.fileno(), xx))
                for conn in conn_table.values():
                    p.register(conn.fileno(),POLLOUT)
                    msg_recv[conn.fileno()] = res_msg

            elif fd == POLLOUT:
                msg = msg_recv[fileno]
                conn.send(msg)
                p.unregister(fileno)
                p.register(fileno,POLLIN)

