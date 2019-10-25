# 在子类派生出的新方法中重用父类功能的方式二：只能在子类中用
# 在python2：super(自己的类名,对象自己)
# 在python3：super()
# 调用super()会得到一个特殊的对象，该特殊的对象是专门用来引用父类中的属性的，!!!完全参照mro列表!!!




# 注意：
# 1. 该方式与继承严格依赖于继承的mro列表
# 2. 访问是绑定方法，有自动传值的效果

class OldboyPeople:
    school='Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyStudent(OldboyPeople):

    #           stu1,'李特丹',18,'female'
    def __init__(self,name,age,sex,num=0):
        # OldboyPeople.__init__(self,name,age,sex) #OldboyPeople.__init__(stu1,李特丹',18,'female')
        super(OldboyStudent,self).__init__(name,age,sex)

        self.score=num

    def choose_course(self):
        print('%s is choosing course' %self.name)



class OldboyTeacher(OldboyPeople):

    def __init__(self,name,age,sex,level):
        super().__init__(name,age,sex)

        self.level=level

    def score(self,stu,num):
        stu.score=num


# stu1=OldboyStudent('李特丹',18,'female') #OldboyStudent.__init__(stu1,'李特丹',18,'female')
# print(stu1.__dict__)
#
# tea1=OldboyTeacher('egon',18,'male',10) ##OldboyTeacher.__init__(tea1,'egon',18,'male',10)
# print(tea1.__dict__)


#例子
class A:
    def test(self):
        print('A.test()')
        super().test()

class B:
    def test(self):
        print('from B')

class C(A,B):
    pass

obj=C()
print(C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
obj.test()
'''
A.test()
from B
'''

