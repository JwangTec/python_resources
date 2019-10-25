# __str__：在对象被打印时自动触发，然后将该绑定方法的返回值(必须是字符串类型)当做本次打印的结果

# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         return '<name:%s age:%s>' %(self.name,self.age)
#
# obj1=People('egon',18)
# obj2=People('lxx',38)
#
# print(obj1) #print(obj1.__str__())
# print(obj2) #print(obj2.__str__())

# l=list([1,2,3])
# print(l)


# __del__：在对象被删除前自动触发, 在该方法内应该执行与该对象有关的系统资源的回收操作
class Foo:
    def __init__(self,filename,encoding='utf-8'):
        self.f=open(filename,'r',encoding=encoding)

    def __del__(self):
        # print('run.....')
        self.f.close()

obj=Foo()
del obj #obj.__del__()
print('其他代码1')
print('其他代码2')
print('其他代码3')
print('其他代码4')
#obj.__del__()