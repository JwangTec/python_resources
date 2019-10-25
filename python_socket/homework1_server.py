
'''
1.客户端读取ipg/png文件，发送给服务器并保存在磁盘上
'''

import socket
import os

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('10.2.0.104',12345))
ss.listen(5)

conn,addr = ss.accept()
print('连接号码：{}'.format(conn.fileno()))
msg = conn.recv(65535)

print('保存文件：{}'.format(msg))
file_load = input('请输入保存文件名：')
file_load += '.png'
f = open(file_load, 'wb')
f.write(msg)
f.close()

print('保存路径:{}'.format(os.path.dirname(__file__)+'/{}'.format(file_load)))







