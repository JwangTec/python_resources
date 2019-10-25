import socket

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('10.2.0.104', 12345))

print('读取icon.png文件：')
fp = open('icon.png', 'rb')

data = fp.read(65535)
ss.send(data)
print(data)
fp.close()
print('发送成功')





