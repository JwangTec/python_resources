# 类中定义的函数有两大类(3小种)用途,一类是绑定方法,另外一类是非绑定方法

# 1. 绑定方法:
# 特点:绑定给谁就应该由谁来调用,谁来调用就会将谁当作第一个参数自动传入
# 1.1 绑定给对象的:类中定义的函数默认就是绑定对象的
# 1.2 绑定给类的:在类中定义的函数上加一个装饰器classmethod


# 2. 非绑定方法
# 特点: 既不与类绑定也不与对象绑定,意味着对象或者类都可以调用,但无论谁来调用都是一个普通函数,根本没有自动传值一说
#


# class Foo:
#     def func1(self):
#         print('绑定给对象的方法',self)
#
#     @classmethod
#     def func2(cls):
#         print('绑定给类的方法: ',cls)
#
#     @staticmethod
#     def func3():
#         print('普通函数')
#
#
# obj=Foo()

# obj.func1()
# print(obj)

# Foo.func2()

# 绑定方法
# print(obj.func1)
# print(Foo.func2)

#非绑定方法
# print(obj.func3)
# print(Foo.func3)



import settings

class Mysql:
    def __init__(self,ip,port):
        self.id=self.create_id()
        self.ip=ip
        self.port=port

    def tell_info(self):
        print('%s:%s:%s' %(self.id,self.ip,self.port))

    @classmethod
    def from_conf(cls):
        return cls(settings.IP, settings.PORT)

    @staticmethod
    def create_id():
        import uuid
        return uuid.uuid4()

# obj=Mysql('1.1.1.1',3306)
# obj.tell_info()


obj1=Mysql.from_conf()

obj1.tell_info()








