from select import poll,select,kqueue,POLLIN,POLLOUT

import socket

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #重启服务器不需要改变端口号
ss.bind(('10.2.0.104',12305))

ss.listen(10)

p = poll()   #别称

p.register(ss.fileno(),POLLIN)  #放入ss的编码 以及事件模式 读 写 错误  注册ss的读事件

conn_table = {}
msg_recv = {}
while True:
    events = p.poll()   #抓取事件，与select.select一样

    for event in events:  #events列表中存储的是元祖，需要解包，存储的是[(ss.fileno(),POLLIN),(conn.fileno(),POLLIN)]
        fileno,fd = event   #fileno:事件编号  fd:事件类型

        if fileno == ss.fileno():   #可能是conn
            conn,addr = ss.accept()
            p.register(conn.fileno(),POLLIN)  #将接收消息内容的事件存入监听中
            conn_table[conn.fileno()] = conn   #将链接存入conn字典中


        else:
            conn = conn_table[fileno]
            if fd == POLLIN:
                msg = conn.recv(1024)      #接收消息内容
                res_msg = '账号：{} \n信息内容：{}'.format(conn.fileno(),msg.decode()).encode() #编写广播内容
                print('{}---{}'.format(conn.fileno(), msg.decode()))   #服务器端口播放
                for conn in conn_table.values():   #将信息保存并把所有conn链接加到写事件中 进行广播信息
                    p.register(conn.fileno(),POLLOUT)
                    msg_recv[conn.fileno()] = res_msg

            elif fd == POLLOUT:
                msg = msg_recv[fileno]
                conn.send(msg)
                p.unregister(fileno)  #删除fileno的所有监听
                p.register(fileno,POLLIN)  #上面删除了全部的监听 只需要删除写监听，所以需要把读监听加上














