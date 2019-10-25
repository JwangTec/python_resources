import socket

import threading


class Client:
    def __init__(self):
        self.cl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.cl.connect((('10.2.0.104',25537)))

    def input_msg(self):
        while True:
            msg = input('请发送消息：')
            self.cl.send(msg.encode())
    def recv(self):
        sser = self.cl.recv(1024)
        print('\n'+ sser.decode()+'\n')

    def run(self):
        clinet1 = threading.Thread(target=self.input_msg)
        clinet2 = threading.Thread(target=self.recv)

        clinet1.start()
        clinet2.start()

        clinet1.join()   #使其进程在未运行时也一直存在
        clinet2.join()


if __name__  == '__main__':
    client = Client()
    client.run()
