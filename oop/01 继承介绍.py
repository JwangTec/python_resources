'''
1、什么是继承
    继承是一种新建类的方式，新建的类称之为子类，被继承的类称之为基类、父类、超类
    继承描述的是一种“遗传”的关系:子类可以重用父类的属性

    在python中的继承注意两点：
        1. 在python中支持一个子类同时继承多个父类，
        2. python中类分为两种：
            新式类：但凡继承object的类，以及该类的子类。。。都是新式类
                在python3中一个类如果没有继承人类类，默认继承object类，即python3中所有的类都是新式类

            经典类: 没有继承object的类，以及该类的子类。。。都是经典类
                在python2中才区分新式类与经典类



2、为何要用继承
    1. 减少代码冗余


3、如何用继承

'''

class Parent1(object):
    pass

# print(Parent1.__bases__)

class Parent2:
    pass

class Subclass1(Parent1,Parent2):
    pass

print(Subclass1.__bases__)


# 1、如何利用继承减少代码冗余？？？

# 2、在继承的背景下，属性查找的优先级
# 3、新式类与经典的区别
