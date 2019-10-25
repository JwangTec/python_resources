import threading

#多线程执行：遇到阻塞（input accept等）会将其进入睡眠，执行下一个程序 若执行时间过长也会睡眠
def test1():
    while True:
        aa = input('输入：\n')
        print(aa)

def test2():
    for i in range(11):
        print(i)


thread_1 = threading.Thread(target=test1)  #将test1交给thread_1执行
thread_1.start()

test2()