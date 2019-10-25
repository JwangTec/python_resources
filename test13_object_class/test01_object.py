'''
面向对象：先有类（抽象）才有对象（具体）
class:
可继承  class Mylist(list):  括号里为其它的对象等   ：可多继承，层层继承，本次继承拥有被继承以及上面所有
继承父类的init时，需要使用supper().__init__()
可重写：可以在继承的类中重写其中的方法或功能（多态）
可扩展：继承中可以增加新的方法或功能
'''
'''
import random
#类的申明方式
class Car:  #可以有无数函数  命名：首字母必须大写

    def __init__(self):        #面向对象中的所有东西可共享（通过self挂载，再通过self调用，只用于类）init中为确定的功能
        self.coloer = 'red'
        self.ppai = 'jili'
        self.kuandu = 1900
        print('对象初始化')
        self.x = random.randint(0,100)

    def test(self):
        print(self.coloer)
        self.laba()
        return self.ppai

    def laba(self):
        self.changd = 8000

    def de_self(self):
        print(self.x)     #挂载在self上，每次调用地址不同
        print(id(self.x))
        xx = random.randint(0,100)  #依附于class上，相当于函数变量，每次调用地址相同
        print(xx)
        print(id(xx))

    def de1_self(self):
        self.de_self()


# car1 = Car()         #类的实例化(对象) 会直接调用类中的__init__（初始化）函数 (魔法函数都以__名称__为命名格式)初始化
# car2 = Car()         #可实例化多次
# #
# # print(car1.test())   #调用功能函数
# # print(car1.coloer)    #调用self的属性
#
# car1.laba()             #属于类里除__init__函数之外的self需要先运行其类中对应的函数，才能挂载在self上，对象才能继续调用
# print(car1.changdu)


self ：相当于挂载器，可以将类中的各个属性通过其挂载，再使用，属于对象，可以在类中互相传递
每个self都有一个独立的空间

car1 = Car()
car1.de_self()
car1.de1_self()
'''

# import random
# class Student:
#     def __init__(self):
#         self.cla_num = random.randint(1,5)
#         self.cla_stunum = random.randint(1,50)
#
#
#     def cla_girls(self):
#         stunum = self.cla_stunum
#         self.girls = random.randint(1,stunum)
#         print("女生人数：%d"%self.girls)
#
#     def cla_boysnum(self):
#         cla_boyssnum = self.cla_stunum - self.girls
#         print("男生人数：%d"%cla_boyssnum)
#
#     def cla_no(self):
#         print("班级号：%d"%self.cla_num)
#
#     def cla_all(self):
#         print("班级总人数：%d"%self.cla_stunum)
#
# student1 = Student
#
# student1.cla_girls()
# student1.cla_no()
# student1.cla_all()
# student1.cla_boysnum()


#私有属性
'''
class Room:
    def __init__(self,name_num):  #初始化时，可以加入参数
        self.__password = 111   #在前面+__后 该属性变成私有，只能在内部调用
        self.__card = 111111
        self.n = name_num

    def card_get(self):      #可以通过函数传出，但可以修改成其它值
        return self.__card / 2

    def get_password(self):
        return '12365'

xx = Room('aaaa')  #参数值传入并初始化

print(xx.card_get())
print(xx.get_password())


#每一个类中都存在默认函数：如__str__(魔法函数，会自动调用)
'''



