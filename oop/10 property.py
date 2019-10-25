'''
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86

'''

# property装饰器就是将一个函数属性伪装成一个数据属性
# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# obj=People('egon',80,1.83)
# # print(obj.bmi())
#
# print(obj.bmi)

# 了解
# class People:
#     def __init__(self,name):
#         self.__name=name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,obj):
#         if type(obj) is not str:
#             print('名字必须是str类型')
#             return
#         self.__name=obj
#
#     @name.deleter
#     def name(self):
#         # print('不让删')
#         del self.__name
#
# obj=People('egon')
# # print(obj.name)
#
# # obj.name='EGON'
# # obj.name=123
# # print(obj.name)
#
# del obj.name
# print(obj.name)




class People:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def set_name(self,obj):
        if type(obj) is not str:
            print('名字必须是str类型')
            return
        self.__name=obj

    def del_name(self):
        # print('不让删')
        del self.__name

    name=property(get_name,set_name,del_name)

obj=People('egon')
print(obj.name)

# obj.name='EGON'
# obj.name=123
# print(obj.name)

# del obj.name
# print(obj.name)