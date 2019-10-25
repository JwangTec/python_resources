#coding:utf-8

# 多继承背景下属性查找的顺序：对象-》对象的类-》按照从左往右的顺序一个一个的分支找下去
#
# #第四层
# class I:
#     # x='I'
#     pass
#
# #第三层
#
# class E:
#     # x='E'
#     pass
#
# class F(I):
#     # x='F'
#     pass
#
# class H:
#     x='H'
#
# # 第二层
# class B(E):
#     # x='B'
#     pass
#
# class C(F):
#     # x='C'
#     pass
#
# class D(H):
#     # x='D'
#     pass
#
# #第一层
# class A(B,C,D):
#     # x='A'
#     pass
#
# obj=A()
# # obj.x=111
# print(obj.x)


# 一旦出现菱形继承问题，新式类与经典类在属性查找上的区别是
# 新式类：广度优先查找，在最后一个分支查找顶级类
# 经典类：深度优先查找，在第一个分支就查找顶级类

class G(object):
    # def test(self):
    #     print('from G')
    pass

# 第三层
class E(G):
    # def test(self):
    #     print('from E')
    pass

class F(G):
    def test(self):
        print('from F')
    pass

# 第二层
class B(E):
    # def test(self):
    #     print('from B')
    pass

class C(F):
    def test(self):
        print('from C')
    pass

class D(G):
    def test(self):
        print('from D')
    pass

# 第一层
class A(B,C,D):
    # def test(self):
    #     print('from A')
    pass

obj=A()
# obj.test()

# 新式类：对象-》A-》B-》E-》C-》F-》D-G
# 经典类：对象-》A-》B-》E-》G-》C-》F-》D


#在新式类中，提供了一个mro方法
# print(A.mro())