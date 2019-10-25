# 继承解决的是类与类之间的代码冗余问题，一定是一个类是另外一个类的子类


# 继承关系的查找
# 总结对象之间的相似之处得到类，总结类与类之间的相似之处就得到了类们的父类

'''


class OldboyPeople:
    school='Oldboy'


class OldboyStudent(OldboyPeople):

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=0

    def choose_course(self):
        print('%s is choosing course' %self.name)



class OldboyTeacher(OldboyPeople):

    def __init__(self,name,age,sex,level):
        self.name=name
        self.age=age
        self.sex=sex
        self.level=level

    def score(self,stu,num):
        stu.score=num
'''


'''


class OldboyPeople:
    school='Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyStudent(OldboyPeople):

    # def __init__(self,name,age,sex):
    #     self.name=name
    #     self.age=age
    #     self.sex=sex
    #     self.score=0

    def choose_course(self):
        print('%s is choosing course' %self.name)



class OldboyTeacher(OldboyPeople):

    # def __init__(self,name,age,sex,level):
    #     self.name=name
    #     self.age=age
    #     self.sex=sex
    #     self.level=level

    def score(self,stu,num):
        stu.score=num


stu1=OldboyStudent('李特丹',18,'female') #OldboyPeople.__init__(stu1,'李特丹',18,'female')
print(stu1.__dict__)

tea1=OldboyTeacher('egon',18,'male') ##OldboyPeople.__init__(tea1,'egon',18,'male',10)
print(tea1.__dict__)
'''





# 问题？？？：如何在子类派生出的新方法中重用父类的功能

class OldboyPeople:
    school='Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyStudent(OldboyPeople):

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=0

    def choose_course(self):
        print('%s is choosing course' %self.name)



class OldboyTeacher(OldboyPeople):

    # def __init__(self,name,age,sex,level):
    #     self.name=name
    #     self.age=age
    #     self.sex=sex
    #     self.level=level

    def score(self,stu,num):
        stu.score=num


stu1=OldboyStudent('李特丹',18,'female') #OldboyPeople.__init__(stu1,'李特丹',18,'female')
print(stu1.__dict__)

tea1=OldboyTeacher('egon',18,'male') ##OldboyPeople.__init__(tea1,'egon',18,'male',10)
print(tea1.__dict__)
