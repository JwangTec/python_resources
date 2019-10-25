# 在子类派生出的新方法中重用父类功能的方式一：
# 指名道姓地访问某一个类的函数
# 注意：
# 1. 该方式与继承是没有关系的
# 2. 访问是某一个类的函数，没有自动传值的效果

class OldboyPeople:
    school='Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyStudent(OldboyPeople):

    #           stu1,'李特丹',18,'female'
    def __init__(self,name,age,sex,num=0):
        OldboyPeople.__init__(self,name,age,sex) #OldboyPeople.__init__(stu1,李特丹',18,'female')

        self.score=num

    def choose_course(self):
        print('%s is choosing course' %self.name)



class OldboyTeacher(OldboyPeople):

    def __init__(self,name,age,sex,level):
        OldboyPeople.__init__(self,name,age,sex)

        self.level=level

    def score(self,stu,num):
        stu.score=num


stu1=OldboyStudent('李特丹',18,'female') #OldboyStudent.__init__(stu1,'李特丹',18,'female')
print(stu1.__dict__)

tea1=OldboyTeacher('egon',18,'male',10) ##OldboyTeacher.__init__(tea1,'egon',18,'male',10)
print(tea1.__dict__)
