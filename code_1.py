'''
逻辑补1
算数补0
右移：111 --> 11
左移：111 --> 1110  （补0）
用处：Linux 文件系统 位运算+或运算+异或运算（01为1 其余为假） r = 1 << 2   w = 1<<1 x= 1<<0   rw = r|w = rwx^x
红黄绿：或运算
红色：100
绿色：010
蓝色：001
红蓝-->紫：101
白色：111
黑色：000

'''

# list1 = [1,2,1,3,2,5]
# total = 0
# for i in list1:
#     total ^= i
#
# print(total)

'''
装饰器:将函数传入到装饰器函数中 也存在
'''
# import functools
# def dec(func):
#     # def Print(n):
#     @functools.wraps(func)   #代称装饰器
#     def Print(*args,**kwargs):
#         """
#
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         print('hello world')
#         return func(*args,**kwargs)
#     return Print
#
# @dec
# def fun1(n):
#
#     return n
#
# @dec
# def fun2(a,b):
#     """
#     :param a:
#     :param b:
#     :return:
#     """
#     return a
#
#
# # fun1 = dec(fun1)  理解该函数的每层调用以及赋值的改变  注意参数的传递
# n =1
# print(fun1(n))
# print(fun2(1,2))    #可变参数的运用
# print(fun1.__name__)  #名称改变了  使用functools函数作为装饰器


# class A(object):
#     def __init__(self, name):
#         self.name = name
#
#     def foo(self, x):
#         print("executing foo(%s, %s)" % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s, %s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % (x))
#
# a = A('alice')
# a.foo('alice')
# A.class_foo('alice')
# a.static_foo('alice')
# A.static_foo('alice')


# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print(" %s is eating" % self.name)
#
#
# d = Dog("ChenRonghua")
# d.eat

# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)


class Animal:
    def __init__(self, name):
        self.name = name


class People(Animal):
    def talk(self):
        print('%s is talking' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s is talking' % self.name)


def func(animal):
    animal.talk()

p=People('alice')
d=Dog('wang')
func(p)
# func(d)