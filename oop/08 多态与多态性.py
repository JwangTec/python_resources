'''
1 多态
    多态指的是同一种事物的多种形态

2 多态性:
    可以在不用考虑对象具体类型的情况下而直接使用对象

    优点:
        归一化,简化对象的使用

'''
# import abc
#
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def speak(self):
#         pass
#
#     @abc.abstractmethod
#     def run(self):
#         pass

#抽象基类:是用来指定规范,但凡继承该类的子都必须实现speak和run,而名字必须叫speak和run
#注意:不能实例化抽象基类
# Animal()


# class People(Animal):
#     def speak(self):
#         print('say hello')
#
#     def run(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         print('汪汪汪')
#
#     def run(self):
#         pass
#
# class Pig(Animal):
#     def speak(self):
#         print('哼哼哼哼哼')
# #
#     def run(self):
#         pass
# #
# obj1=People()
# obj2=Dog()
# obj3=Pig()
#
#obj1,obj2,obj3都是动物
# obj1.speak()
# obj2.speak()
# obj3.speak()

#
# def speak(animal):
#     animal.speak()
#
#
# speak(obj1)
# speak(obj2)
# speak(obj3)


# obj1=[1,2,3]
# obj2='hello'
# obj3={'x':1}
#
# print(obj1.__len__())
# print(obj2.__len__())
# print(obj3.__len__())
#
#
# print(len(obj1))
# print(len(obj2))
# print(len(obj3))



# python崇尚鸭子类型


class Txt:
    def read(self):
        print('txt read')

    def write(self):
        print('txt write')


class Process:
    def read(self):
        print('Process read')

    def write(self):
        print('Process write')


class Disk:
    def read(self):
        print('Disk read')

    def write(self):
        print('Disk write')


obj1=Txt()
obj2=Process()
obj3=Disk()



obj1.read()
obj1.write()

obj2.read()
obj2.write()

obj3.read()
obj3.write()