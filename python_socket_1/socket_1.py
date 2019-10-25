import socket
import select
import threading

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ss.connect(('14.215.177.38',80))

def send_http():
    ss.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n'.encode())

    msg = ss.recv(10240)

    print(msg.decode())

ss1 = threading.Thread(target=send_http)
ss2 = threading.Thread(target=send_http)


ss1.start()
ss2.start()