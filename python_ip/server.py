import socket
#socket.AF_INET --> ip,ip6
# socket.SOCK_STREAM  --> tcp,udp
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('10.2.0.26',19528))
#最大能监听10个人同时进来
ss.listen(10)
print('服务已经启动')
while 1:
    conn,addr = ss.accept()
    print(conn)
    while 1:
        msg = conn.recv(1024)
        print(msg)
        conn.send(b'i have recived your msg')




