import socket
import select

#select 监听 读 写 错误 所有事件

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print('初始化----------')

ss.bind(('10.2.0.104',12332))

ss.listen(10)

readlist =[ss]
writelist = []

msg_dict ={}
conn_list = []   #存放所有conn链接
msg_dict_code = {}  #存放消息
# conn,addr = ss.accept()
while True:  #让其一直循环监听
    rlist,wlist,xlist = select.select(readlist,writelist,[])

    #监听readlist列表中的事件ss的读 只要右边的readlist读 有事件发生就会向下执行 可监听readlist列表中的所有元素
    #rlist 中只会存在本次 readlist中有事件发生的已经准备好的事件
    #只要rlist wlist xlist中任何一个存在值就会向下执行

    for r in rlist:
        if r is ss:
            conn,addr = r.accept()
            conn_list.append(conn)
            readlist.append(conn)   #添加事件conn到读事件列表中去，使读能监听ss和conn这两个事件

        else:
            msg = r.recv(1024)
            # msg_dict[r.fileno()] = msg  #将消息内容放入字典中  只存了这一个的消息
            if len(msg) == 0:
                r.close()
                readlist.remove(r)   #若客户端断开链接 则不再监听该conn
                conn_list.remove(r)
            print('{}-----{}'.format(r.fileno(),msg.decode()))

            msg = "编号：{} 信息内容: {}".format(r.fileno(),msg.decode())


            for i in conn_list:
                writelist.append(i)     #将所有conn放入写监听中
                msg_dict_code[i.fileno()] = msg  #将所有相对应的消息存入

    for w in wlist:
        msg = msg_dict_code[w.fileno()]
        w.send(msg.encode())   #有写事件发生则发送收到的消息
        del msg_dict_code[w.fileno()]     #删除该编号记录的信息
        writelist.remove(w)  #将该w事件从监听中移除  不然会一直发送
