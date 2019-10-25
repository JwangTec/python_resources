'''
class StudentError(Exception):
    pass


class GroupError(Exception):
    pass


class Student:
    def __init__(self, group_name, no, name, age, score):
        self.group_name = group_name
        self.no = no
        self.name = name
        self.age = age
        self.score = score

    def get_score(self):
        return self.score

    def __str__(self):
        return "学生学号:{} 学生姓名:{} 学生年龄:{} 学生分数:{}".format(self.no, self.name, self.age, self.get_score())


class Group:
    def __init__(self, name):
        self.name = name
        self.members = set()

    def add_member(self, student):
        if not isinstance(student, Student):
            raise StudentError('加入学生组的必须是学生对象')
        self.members.add(student)


class Excel:
    def __init__(self):
        self.subject = ('Computer', 'Math', 'Chinese', 'Star', 'Python')
        self.groups = {name: Group(name) for name in self.subject}
        self.no = 1

    def __add_student(self, group_name, name, age, score):
        group = self.groups.get(group_name, None)
        if group is None:
            raise GroupError('没有这个group')
        student = Student(group_name, self.no, name, age, score)
        group.add_member(student)
        self.no += 1

    def __del_student(self, no):
        for group in self.groups.values():
            for student in group.members:
                if int(student.no) == int(no):
                    group.members.remove(student)
                    return True
        else:
            return False

    def del_student(self):
        no = input("请输入你要删除学生的学号: ")
        if self.__del_student(no):
            print('删除成功')
        else:
            print("删除失败")

    def get_group_info(self):
        group_name = input("请输入小组名: ")
        group = self.groups.get(group_name, None)
        if group is None:
            raise GroupError('没有这个group')
        print('|{}|'.format('-' * 50))
        print('|组名 {} \n|组成员的详细信息如下'.format(group.name))
        score = 0
        student_num = len(group.members)
        sort_members = sorted(group.members, key=lambda student: student.no)
        for student in sort_members:
            print('|' + str(student) + '')
            score += int(student.get_score())
        if student_num == 0:
            print('|小组人数:0 小组总成绩:0 小组平均成绩:0')
        else:
            print('|小组人数:{} 小组总成绩:{} 小组平均成绩:{}'.format(student_num, score, score / student_num))

    def get_info(self):
        for k, v in self.groups.items():
            print('|{}|'.format('-' * 50))
            print('|组名 {} \n|组成员的详细信息如下'.format(k))
            score = 0
            student_num = len(v.members)
            for student in v.members:
                print('|' + str(student) + '')
                score += int(student.get_score())
            if student_num == 0:
                print('|小组人数:0 小组总成绩:0 小组平均成绩:0')
            else:
                print('|小组人数:{} 小组总成绩:{} 小组平均成绩:{}'.format(student_num, score, score / student_num))
            print('|{}|'.format('-' * 50))
        print('*************************************')

    def __select(self, min_value, max_value, select_type):
        if select_type != 'score':
            select_type = 'age'
        student_list = list()
        for group in self.groups.values():
            for student in group.members:
                if min_value <= int(getattr(student, select_type)) <= max_value:
                    student_list.append(student)
        print('符合要求的学生有：')
        for student in student_list:
            print(student)

    def select_student(self):
        select_type = input('请输入你要查找的类型 age|score:')
        min_value = int(input('请输入最小值'))
        max_value = int(input('请输入最大值'))
        self.__select(min_value, max_value, select_type)

    def add_student(self):
        print('当前的小组有 {}'.format(self.subject))
        group_name = input("请输入学习组名字: ")
        name = input("请输入学生的名字: ")
        age = input("请输入学生的年龄: ")
        score = input("请输入学生的成绩: ")
        try:
            self.__add_student(group_name, name, age, score)
        except GroupError as e:
            print("添加小组失败 失败原因:{} 请重新添加".format(e))
        except StudentError as e:
            print("添加学生失败 失败原因:{} 请重新添加".format(e))

    def run(self):
        while True:
            select_num = input("请选择功能\n1. 添加学生 \n2. 删除学生 \n3. 打印小组信息 \n4. 显示所有信息\n5. 筛选学生信息 \n0. 退出 \n 请输入: ")
            select_num = int(select_num)
            if select_num == 1:
                self.add_student()
            elif select_num == 2:
                self.del_student()
            elif select_num == 3:
                try:
                    self.get_group_info()
                except GroupError:
                    print('小组名错误')
            elif select_num == 4:
                self.get_info()
            elif select_num == 5:
                self.select_student()
            elif select_num == 0:
                break
            else:
                print('请重新输入')
                continue

        print('成功退出')


if __name__ == "__main__":
    e = Excel()
    e.run()

'''


# list1 = [str(a)+b for a in range(0,11) for b in ['a','b','c','d','e','f','g','h','j']]
# print(list1)
import os
# def deep_list(dir):
#     lists = os.listdir(dir)
#     if not os.path.isdir(dir):
#         return
#     for d in lists:
#         print(d)
#         deep_list(os.path.join(dir,d))
#
# deep_list('test')

# def brand_first(dir):
#     buckets = []
#     buckets.append(dir)
#
#     while len(buckets):
#         tmp = buckets.pop(0)
#         print(tmp)
#         files = os.listdir(tmp)
#         files.sort()
#         for i in files:
#             buckets.append(os.path.join(tmp,i))
#
# brand_first('test')

# import re
#
# pattern = re.compile(r'\d+')
#
# print(pattern.split('one1two2three')) #以此分隔并返回分开后的形式
#
# print(pattern.match('0one1two2three'))  #返回一个对象
#
# print(pattern.findall('one111two211three')) #返回所有能匹配的对象
#
# print(pattern.finditer('one1two2three'))   #返回为迭代器
#
# pattern1 = re.compile(r'(\d\w+) (\d\w+)')  #相互交换位置
# print(pattern1.sub(r'\2 \1','1one 2two'))

# my_dict = {}
#         for i in range(len(nums)):
#             if target-nums[i] not in my_dict:
#                 my_dict[nums[i]] = i
#             else:
#                 return [my_dict[target-nums[i]], i]
