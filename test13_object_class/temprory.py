
'''
class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def gender1(self):
        if self.gender == 1:
            return '男'
        else:
            return '女'

class Student(Person):
    list1 = []
    dict1 = {}
    def __init__(self,name,gender,age,scores):
        super().__init__(name,gender,age)
        self.scores = scores
        Student.list1.append(self.name)
        Student.dict1[self.name] = self.scores

    def is_score(self,name,scores1):
        if scores1 > 100 or scores1 < 0:
            raise TypeError('xxx')
        else:
            Student.dict1[name] = scores1
            self.scores = scores1
            return self.scores

    def name1(self):
        return Student.list1

    def score1(self):
        return Student.dict1

class Teacher(Person):
    def __init__(self,name,gender,age,salary):
        super().__init__(name,gender,age)
        self.__salary = salary





s1 = Student('a',1,59,100)
s1.is_score('a',90)
s2 = Student('b',1,22,90)
s3 = Student('c',1,22,90)

list_student = s3.list1
student = s3.dict1

def avg_sum(dict1):
    xx = len(dict1)
    sum = 0
    for _,v in dict1.items():
        sum += v
    avg = sum / xx
    return avg
'''



