import socket
import threading
class Client:
    def __init__(self):
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.connect(('10.2.0.104', 12306))
        self.run_client = True


    def input_msg(self):
        print('请在下方输入需要发送的内容\n')
        while self.run_client:
            msg = input()+"@叮当猫"
            self.ss.send(msg.encode())

    def recv_msg(self):
        while self.run_client:
            msg = self.ss.recv(1024)
            print(msg.decode())
            print('-------------------')

            if len(msg) == 0:
                print('服务端已经断开链接')
                self.run_client = False

    def run(self):
        task1 = threading.Thread(target=self.input_msg)
        task2 = threading.Thread(target=self.recv_msg)
        task1.start()
        task2.start()
        task1.join()
        task2.join()

if __name__ == '__main__':
    c = Client()
    c.run()