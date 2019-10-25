import socket

#socket.AF_INET --> ip,ip6
#socket.SOCK_STREAM --> tcp.udp
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #初始化socket 使用ip tcp协议
ss.bind(('10.2.0.190',11111)) #绑定本机应用 本机地址+端口号

ss.listen(10)  #最大能监听10人同时进来
print('start ::::::::::::')
while 1:
    addr,conn = ss.accept()  #服务器接收链接  conn：服务器连接通道（多个）+ 地址
    print(conn)
    while 1:
        msg = conn.recv(1024)  #一次性接收消息的字节数 1024
        if len(msg) == 0:
            break
        print(msg)
        conn.send(b'i have aadffaf') #服务器将消息发送给客户端

