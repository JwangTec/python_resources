# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
#
# obj=Bar()
#
# # print(isinstance(obj,Bar))
# # print(isinstance([],list))
#
# print(issubclass(Bar,Foo))



# 反射:指的是通过字符串来操作属性
class Foo:
    def __init__(self,name):
        self.name=name


obj=Foo('egon')


# hasattr()
# print(hasattr(obj,'name')) #'name' in obj.__dict__

# getattr()
# print(getattr(obj,'name')) #obj.__dict__['name']
# print(getattr(obj,'age')) #obj.__dict__['age']
# print(getattr(obj,'age',None)) #obj.__dict__['age']

# setattr()
# setattr(obj,'age',18) #obj.age=18
# setattr(obj,'name','EGON') #obj.name='EGON'
# print(obj.__dict__)

# delattr()
# delattr(obj,'name')# del obj.name
# print(obj.__dict__)



class Ftp:
    def get(self):
        print('get')

    def put(self):
        print('put')

    def login(self):
        print('login')

    def run(self):
        while True:
            choice=input('>>>: ').strip()
            if hasattr(self,choice):
                method=getattr(self,choice)
                method()
            else:
                print('命令不存在')


obj=Ftp()
obj.run()