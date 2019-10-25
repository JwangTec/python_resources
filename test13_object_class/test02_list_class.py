class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n

class MyList:
    def __init__(self, *args):
        self.first_node = Node(None, None)
        self.length = 1
        for i in args:
            self.append(i)
        self.listxx = args

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
        return node.value

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

    def __gt__(self, other):  #other表示另一个对象，self表示本次的对象   __gt__(>)  __at__(<)
        if self.length > other.length:
            return True
        else:
            return False
    def __add__(self, other):

        len1 = len(self)
        len2 = len(other)
        l3 = MyList()
        for i in range(len1):
            l3.append(self.get(i))

        for j in range(len2):
            l3.append(other.get(j))

        return l3

#
#
l1 = MyList(1,2,3,4,5,6)
print(l1.get(2))
l2 = MyList(1,2,3,4)
print(l1+l2)

# l.reverse()
# #l1.remove(77)
# # l.insert(10,77)
# # l.clear()
# #
# # l = [9,2,9,4,9,2,7,8,9]
# # print(l.index(9))
# # print(l1.index(9))
#
# # print(l1)
# print(l)
# print(len(l))
#
#
# class MyListV2(MyList):
#     def sort(self):
#         pass
#
#
# class MyListV3(MyListV2):
#     def reverse(self):
#         pass
#
#
# l = MyListV2(6, 7, 8, 9, 10)
#
# l.append(9)





