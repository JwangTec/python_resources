

# 单继承背景下属性查找的顺序：对象-》对象的类-》父类-》。。。
# class Foo:
#     # x=333
#     pass
#
# class Bar(Foo):
#     # x=222
#     pass
#
# obj=Bar()
# # obj.x=111
# print(obj.x)


class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1() #obj.f1()

class Bar(Foo):
    def f1(self):
        print('Bar.f1')


obj=Bar()
obj.f2()
'''
Foo.f2
Bar.f1
'''