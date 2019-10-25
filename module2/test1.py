def a_test():
    return 'a.py'

def test():     #return 为空 调用会多一个返回值空，以及执行该函数打印出aaaa
    print("aaaaa")

if __name__ == "__main__":
    print("不可被引用的命令test1")

print('可以被调用的test1')