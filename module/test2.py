from module.test1 import a_test,test  #引用来自module包下test1.py中的a_test函数，module包必须含有_init_.py文件

def b_test():
    return 'b.py'

print(a_test())   #输出test1中的a_test函数运行结果
print(test())