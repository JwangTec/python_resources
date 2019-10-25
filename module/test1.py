'''
小技巧，程序自动识别当前执行的python文件名   __file__
'''

def a_test():
    return 'a.py'

def test():     #return 为空 调用会多一个返回值空，以及执行该函数打印出aaaa
    print("aaaaa")

if __name__ == "__main__":   #该命令下的不会被引用执行
    print("不可被引用的命令test1")

print('可以被调用的test1')