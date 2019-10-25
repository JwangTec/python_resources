'''
基础

class Person:

    def __init__(self,name,age,id):
        self.__age = age       #私有属性：进行运行时无法查看（被保护）,可隐藏真实数据
        self.__name = name
        self.id = id


    def age(self):
        return self.__age//2

    def set_age(self,age):  #判断输入的参数是否符合规则，符合就修改该参数
        if age < 50:
            self.__age = age
        else:
            self.__age = 50

        return self.__age


    @property  # 可以直接使用函数名调用的内置装饰器
    def name(self):
        return self.__name

    def id_c(self):
        print(self.id)


p = Person('xxx',50,12)

print(p.age())  #只能通过函数调用该属性，并且函数能改原数据

print(p.name)   #不需要加（）即可调用该函数

p.id = 14    #可修改类中的参数。
p.id_c()

p.set_age(30)   #判断参数规则并修改该参数
print(p.age())

'''

class DataBaset:
    #在设置属性时会直接调用，控制其对象只能存在的属性
    __slots__ = ('__password','__database_name','__name')

    def __init__(self):
        self.__name = ''
        self.__password = ''
        self.__database_name = ''

    def name(self):
        return self.__name
    @property   #将函数变成属性  若有相关联的setting则需要对setting中的语句再执行该变量
    def password(self):
        return "{}".format('*' * len(self.__password))

    def set_name(self,name):
        iswasp = True
        while iswasp == True:
            if type(len(name)) == str:
                print("非字符串")
                iswasp = False
            elif len(name) < 6:
                print('账户名错误')
                iswasp = False
            elif 48 <= ord(name[0])<= 57:
                print("首字母为数字")
                iswasp = False
            else:
                self.__name = name
                break
    @password.setter   #在变成属性的函数赋值时会调用此setting函数
    def password(self,password):
        if type(password) != str:
            print('错误')
            return
        if len(password) < 8:
            print('长度不够')
            return
        self.__password = password


mysql = DataBaset()



# mysql.name = 'aaaaaa'  #未修改类中的任何，只是单纯定义（直接在类中设置控制函数就可）

'''
在使用property后 如果需要直接使用赋值语法修改被保护的，可在相关判断条件下使用  
@判断名(需要与函数名一样).setter
'''
mysql.password = 'aaa'
print(mysql.password)
