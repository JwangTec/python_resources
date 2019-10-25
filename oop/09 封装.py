'''
1 什么是封装
    装就是将数据属性或者函数属性存放到一个名称空间里
    封指的是隐藏,该隐藏是为了明确地区分内外,即该隐藏是对外不对内(在类外部无法直接访问隐藏的属性,而在类内部是可以访问)


2 为何要封装
    1. 封数据属性:???
    2. 封函数属性:???

3 如何封装???
    在类内定义的属性前加__开头
'''


# class People:
#     __country='China' #_People__country='China'
#     __n=111           #_People__n=111
#
#     def __init__(self,name):
#         self.__name=name #self._People__name=name
#
#     def run(self):
#         print('%s is running' %self.__name) #self._People__name

# print(People.__country)

# obj=People('egon')
# print(obj.__name)
# print(obj.run)
# obj.run()

# print(People.__dict__)
# print(People._People__country)
# print(obj.__dict__)
# print(obj._People__name)


# 总结这种隐藏需要注意的问题:
# 1. 这种隐藏只是一种语法上的变形,并没有真的限制访问
# 2. 这种变形只在类定义阶段检测语法时变形一次,类定义阶段之后新增的__开头的属性不会发生变形
# People.__x=1
# obj.__y=2

# print(People.__dict__)
# print(obj.__dict__)

# 3. 在继承中，父类如果不想让子类覆盖自己的方法，可以在该方法前加__开头
# class Parent1:
#     def __func(self): #_Parent1__func
#         print('parent1.func')
#
#
# class Sub1(Parent1):
#     def __func(self): #_Sub1__func
#         print('sub1.func')


# class Foo:
#     def __f1(self): #_Foo__f1
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.__f1() #self._Foo__f1()
#
# class Bar(Foo):
#     def __f1(self): #_Bar__f1
#         print('Bar.f1')
#
#
# obj=Bar()
# obj.f2()


# 封装的真实意图:把数据属性或函数属性装起来就是为了以后使用的,封起来即藏起来是为不让外部直接使用
# 1.封数据属性:把数据属性藏起来,是为了不让外部直接操作隐藏的属性,而通过类内开辟的接口来间接地操作属性,
#             我们可以在接口之上附加任意的控制逻辑来严格控制使用者对属性的操作

'''
class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('<name:%s age:%s>' % (self.__name, self.__age))

    def set_info(self, name, age):
        if type(name) is not str:
            print('名字必须是str类型')
            return
        if type(age) is not int:
            print('年龄必须是int类型')
            return

        self.__name = name
        self.__age = age


obj = People('egon', 18)

# obj.tell_info()
# obj.set_info('EGON',19)
# obj.set_info(123,19)
obj.set_info('EGOn','19')
obj.tell_info()
'''

#2. 封函数属性: 隔离复杂度
class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()
a.withdraw()