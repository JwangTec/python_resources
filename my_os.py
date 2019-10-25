# import os
# import time
# import datetime
# print(time.sleep(2)) #暂停2秒

# print(time.time()) #时间戳
#
# print(datetime.time())

import random

#
# print(random.randint(0,10)) #伪随机
# print(random.random())
# #
# import requests
# r = requests.get('https://www.163.com')
# #
# print(r.text)

# from module import a
#
# print(a.a_test())

# from p1904.u import test
# test()

# 文件的读取
# r w a -->读 写 追加写
# 系统级调用
# with open('open.txt','r') as f:
#     text = ""
#     while True:
#         x = f.readlines()
#         if len(x) == 0:
#             break
#         print(x)
# print(text)


# car = {
#     "pingpai":'jili',
#     'changdu':5200,
#     'kuandu':1800,
#     'gaodu':1400,
#     'yanse':'红色',
#     '按喇叭':test()
# }

# class   # object


# 类的申明方式
import random


# class Car:
#     # 这个特殊函数 他会在函数启动的时候偷偷调用 魔法函数
#
#     def __init__(self):
#         self.pingpai = 'jili'
#         self.changdu = 5200
#         self.kuandu = 1800
#         self.yanse = 'hongse'
#         print('对象初始化过程')
#
#     def test(self):
#         # print(self.pingpai)
#         x = random.random()
#         print(x)
#         print(id(x))
#
#     def laba(self):
#         self.test()
#
#
# # 类的实例化
# car = Car()
# car1 = Car()
# car.test()
# car1.test()

# print(car.pingpai)
# car.test()
# print(car.luntai)
# car1 = Car()
# car2 = Car()
# print(id(car))
# print(id(car1))
# print(id(car2))

# 一个班 1。 班机号 2。 班级人数 3。 班级男女人数 《---都是随机的
# 函数 1。 获取班级的号  2。 获取班级人数  3。 获取班级男生数量
# import random
# class ClassRoom:
#
#     def __init__(self):
#         self.no = random.randint(1,20)
#         self.student_num = random.randint(20,40)
#         self.female_num = random.randint(10,30)
#         self.male_num = self.student_num - self.female_num
#
#     def get_class_no(self):
#         return self.no
#
#     def get_total_num(self):
#         return self.student_num
#
#     def get_male_num(self):
#         return self.male_num
#
# classroom1 = ClassRoom()
# classroom2 = ClassRoom()
#
# print(classroom1.get_class_no())
# print(classroom2.get_class_no())

# class Qiaobiluo:
#     def __init__(self,platform):
#         self.__age = 50
#         self.__skin = 'black'
#         self.__face = 'pretty ugly'
#         self.p = platform
#     def get_age(self):
#         return self.__age/2
#     def get_skin(self):
#         return 'white'
#     def get_face(self):
#         return 'beautiful'
#     def get_platform(self):
#         return self.p
#     def __str__(self):
#         return '宇宙无敌'
# q = Qiaobiluo(None)
# print(q.get_platform())

class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n


# x = [1,2,3,5,6,7,8,9]
# del x[1]
# print(x)
#
# x.pop(0)

x = list


class MyList:
    def __init__(self, *args):
        self.first_node = Node(None, None)
        self.length = 1
        for i in args:
            self.append(i)

    def __len__(self):
        return self.length - 1

    def append(self, v):
        """
        给列表添加一个新的元素
        :param v:
        :return:
        """
        node = self.find_last_node()
        node.next = Node(v, None)
        self.length += 1

    def find_last_node(self):
        """
        找到最后一个元素
        :return:
        """
        node = self.first_node
        if node is None:
            return None
        while True:
            if node.next is None:
                break
            node = node.next
        return node

    def pop(self, index=-1):
        """
        把列表最后一个元素删除
        :return:
        """
        if self.length <= 1:
            return False
        if index == -1:
            index = self.length - 2
        n = self.get(index)
        next = n.next  # 要删除元素的最后一个元素
        pre = self.get(index - 1)  # 要删除元素前面一个元素
        pre.next = next
        self.length -= 1

    def get(self, index):
        index += 1
        if index >= self.length:
            return False
        counter = 0
        node = self.first_node
        if counter == index:
            return node
        while counter != index:
            counter += 1
            # 找到下一个元素
            node = node.next
        return node

    def clear(self):
        self.first_node.next = None
        self.length = 1

    def count(self, value):
        counter = 0
        node = self.first_node.next
        while True:
            if node is not None:
                if node.value == value:
                    counter += 1
                node = node.next
            else:
                break
        return counter

    def remove(self,value):
        pre_node = self.first_node
        current_node = pre_node.next
        while True:
            if current_node is None:
                raise ValueError("{} not in {}".format(value,self.__class__.__name__))
            if current_node.value == value:
                pre_node.next = current_node.next
                return
            pre_node = pre_node.next
            current_node = current_node.next

    def index(self, value):
        """
        找出value所在的第一个节点
        :param value:
        :return:
        """
        counter = 0
        node = self.first_node.next
        while True:
            if node is not None:
                if node.value == value:
                    return counter
                else:
                    counter += 1
                    node = node.next
            else:
                raise ValueError("{} is not in list".format(value))

    def insert(self, index, value):
        counter = 0
        pre_node = self.first_node
        while True:
            if pre_node is None:
                self.append(value)
                break
            if counter == index:
                next_node = pre_node.next
                new_node = Node(value, None)
                pre_node.next = new_node
                new_node.next = next_node
                self.length += 1
                break
            else:
                counter += 1
                pre_node = pre_node.next

    def __str__(self):
        string = "["
        node = self.first_node.next
        if node is not None:
            v = node.value
            string += str(v)
            node = node.next
            while node is not None:
                string += ", " + str(node.value)
                node = node.next
        string += "]"

        return string

    def reverse(self):
        counter = 0
        while self.length-2 > counter:
            node = self.first_node.next
            if node is None:
                return
            self.insert(self.length-1-counter,node.value)
            counter += 1
            self.pop(0)
    # timsort
    # <__main__.MyListV2 object at 0x103aa1bd0>
    # def __str__(self):
    #     global __name__
    #     string = "<"
    #     string += __name__
    #     string += ".MyList"
    #     string += '  object at {0:x}'.format(id(self))
    #     string += ">"
    #     return string
    def __getitem__(self, item):
        if item == -1:
            item = self.length - 2
        node = self.get(item)
        return node.value

    def __delitem__(self, *args, **kwargs):  # real signature unknown
        """ Delete self[key]. """
        self.pop(args[0])


#
#
l = MyList(1,2,3,4,5,6)
l1 = [9, 2, 9, 4, 9, 2, 7, 8, 9]
l.reverse()
#l1.remove(77)
# l.insert(10,77)
# l.clear()
#
# l = [9,2,9,4,9,2,7,8,9]
# print(l.index(9))
# print(l1.index(9))

# print(l1)
print(l)
print(len(l))


class MyListV2(MyList):
    def sort(self):
        pass


class MyListV3(MyListV2):
    def reverse(self):
        pass


l = MyListV2(6, 7, 8, 9, 10)

l.append(9)
