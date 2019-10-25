
import socket
#socket.AF_INET --> ip,ip6
# socket.SOCK_STREAM  --> tcp,udp
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ss.connect(('10.2.0.26',19527))

while 1:
    msg = input('请输入消息:')
    ss.send(msg.encode())
    msg = ss.recv(1024)
    print(msg)
