'''
1、什么是组合
    组合指的是一个对象拥有某一个属性，该属性的值是另外一个类的对象
    obj=Foo()

    obj.attr1=Bar1()
    obj.attr2=Bar2()
    obj.attr3=Bar3()

2、为何用组合
    为了减少类与类之间代码冗余

3、如何用

'''
class OldboyPeople:
    school='Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyStudent(OldboyPeople):

    def __init__(self,name,age,sex,):
        super().__init__(name,age,sex)
        self.score=0
        self.courses=[]

    def choose_course(self):
        print('%s is choosing course' %self.name)

    def tell_all_course(self):
        for course_obj in self.courses:
            course_obj.tell_info()


class OldboyTeacher(OldboyPeople):

    def __init__(self,name,age,sex,level):
        super().__init__(name,age,sex)
        self.level=level


    def score(self,stu,num):
        stu.score=num

class Course:
    def __init__(self,c_name,c_price,c_period):
        self.c_name = c_name
        self.c_price = c_price
        self.c_period = c_period

    def tell_info(self):
        print('<课程名:%s 价钱:%s 周期:%s>' %(self.c_name,self.c_price,self.c_period))

# 创建课程
python_obj=Course('Python全栈开发',19800,'5mons')
linux_obj=Course('Linux架构师',10000,'3mons')


stu1=OldboyStudent('李特丹',18,'female')
stu2=OldboyStudent('张全蛋',38,'male')
stu3=OldboyStudent('刘二蛋',48,'male')

'''
# 一个学生只选修一门课程

stu1.course=python_obj
stu2.course=python_obj
stu3.course=python_obj


# print(stu1.course.c_name,stu1.course.c_price,stu1.course.c_period)
# print(stu2.course.c_name,stu2.course.c_price,stu2.course.c_period)
# print(stu3.course.c_name,stu3.course.c_price,stu3.course.c_period)

stu1.course.tell_info()
stu2.course.tell_info()
stu3.course.tell_info()
'''
# 一个学生可以选修多门课程

stu1.courses.append(python_obj)
stu1.courses.append(linux_obj)
stu2.courses.append(python_obj)
stu2.courses.append(linux_obj)


stu1.tell_all_course()
stu2.tell_all_course()








# tea1=OldboyTeacher('egon',18,'male') ##OldboyPeople.__init__(tea1,'egon',18,'male',10)
# print(tea1.__dict__)
