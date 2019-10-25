'''
装饰器:只要存在@则会直接运行，除非装饰器中含有函数需要调用
避免该情况：在装饰器中包一层函数

'''
'''
def dec(fun):
    print("dec running")
    return fun
@dec               #@装饰器与下方一样 == 语法糖
def tar():
    print('tar')

# tar  = dec(tar)  #相当于给tar附加了一个功能：该功能在dec中运行
# tar()

tar()
'''

reg = []

def regfun(func):
    def test():
        print('fun reg %s' % func.__name__)
        reg.append(func)
        print(reg)
    return func

@regfun  #相当于regfun = dec(fegfun)
def f1():
    print('f1...>')

def f2():
    print('f2...>')


#   *  若其变量是可拆包的列表等，可以直接使用*号
def test(a,b,c,d,num1 = 3,nu2 = 4):    #可以在其中加上默认值,默认参数写在末尾，其无顺序规则
    return a + b + c + d + num1 + nu2

l = [1,2,3,4]
print(test(*l))

def list2(*args):
    return sum(args)
list1 = [5,1,1,1]
print(list2(*list1))

# ** 其变量为字典时，将其拆分。
list3 = {'a':1,'b':2}
def list_3(**num):
    print(num)
list_3(**list3)


