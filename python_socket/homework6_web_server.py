import socket
import os

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ss.connect(('14.215.177.38',80))

def send_http():
    ss.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n'.encode())
    msg = ss.recv(10240)
    return msg

def file_copy(msg):
    load_copy = input('请输入保存文件名：')
    load_copy += '.txt'
    fp = open(load_copy,'w')
    fp.write(msg.decode())
    fp.close()

    load = os.path.dirname(__file__) + '/{}'.format(load_copy)
    print('报文保存路径：{}'.format(load))

xx = send_http()
file_copy(xx)