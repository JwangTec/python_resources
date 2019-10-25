
import socket
#socket.AF_INET --> ip,ip6
# socket.SOCK_STREAM  --> tcp,udp
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ss.connect(('10.2.0.104',12345))  #连接服务器的地址+端口号


msg = input('请输入消息:')
ss.send(msg.encode())  #发送消息给服务器 转化为utf8 二进制发送
msg = ss.recv(1024)   #接收服务器端的tcp内容 字节数为1024
print(msg.decode())   #解码
