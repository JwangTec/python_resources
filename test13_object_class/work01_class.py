
# 作业：
# 1、
# 新创建一个Student类，该类的实例包含属性
# （姓名 name，性别gender，年龄age，身份证号code，身高height，体重）

'''
class Student:
    def __init__(self,height,age):
        self.name = ""
        self.gender = ""
        self.age = age
        self.code = ""
        self.height = height
        self.weight = ""

    def __gt__(self, other):
        return self.height*1.5 > other.height

guojinming = Student(120,30)
huangxiaoming = Student(160,40)

# if guojinming>huangxiaoming:
#     print('郭敬明高')
# else:
#     print('黄晓明高')

# print('A'>'B')
'''

# 给学生类增加一个比较2名学生身高的方法，打印最高的身高；
#
# 新创建一个Teacher类，该类的实例包含属性：姓名、年龄、学生（Student对象）；
# 1）写一个方法：计算老师与学生年龄的差值；
# 2）添加一个老师的行为(方法)，打印输出该老师的口头禅；
'''
class Teacher:
    def __init__(self,name,age,student):
        self.name = name
        self.age = age
        self.student = student

    def count_age(self):
        return self.age - self.student.age

    def speak(self):
        print('毛主席说')

t = Teacher('fff',60,huangxiaoming)

print(t.speak())
'''
# # 2、
# 定义一个圆形类，已知半径，可提供计算圆形的周长和面积
# # 定义一个圆环类，已知外半径和内半径，可提供计算圆环周长和面积
'''
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * math.pi

    def length(self):
        return self.radius*2*math.pi

class Ring:
    def __init__(self,inner_radius,outer_radius):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.inner_circle = Circle(self.inner_radius)
        self.outer_circle = Circle(self.outer_radius)
    def area(self):
        return abs(self.inner_circle.area() - self.outer_circle.area())


r = Ring(10,20)
print(r.area())

'''

# 3、编写一个学校教学管理系统，学校中有教师、学生、教务、领导等角色；
# 教师：特性（姓名、年龄、性别、身份证号、授课内容）、行为（授课、吃饭）
# 学生：特性（姓名、年龄、性别、学号、所学内容、爱好）、行为（学习、玩、吃饭）
# 教务：特性（姓名、年龄、性别、所属班级）、行为（抓学习、吃饭、睡觉）
# 领导：特性（姓名、年龄、性别）、行为（专说口头禅、开会、吃饭、打麻将）
# 要求：分析题意，为他们找一个父类，创建各个对象及完成初始化方法，并调用各自的行为；
#
'''
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eat(self):
        print('吃饭')

class Teacher(Person):
    def __init__(self,*args,p_id=None,**kwargs):
        super().__init__(*args,kwargs)
        self.id = p_id

    def teach(self):
        pass
'''
# # 4、写1个项目经理类.
# 属性: 姓名、 基本工资、项目分红(默认10000)、项目奖金.
# 行为: 介绍自己的方法. 叫xx 每月薪水是多少.


# 再写1个软件工程师类.
# 属性: 姓名、基本工资、项目奖金.
# 行为: 介绍自己的方法. 叫xx 每月薪水是多少

'''
class Person:
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def introduction(self):
        raise NotImplemented('还没有自我介绍')

class E(Person):
    def introduction(self):
        print('我是一个软件工程师')

class M(Person):
    def introduction(self):
        print('我是一个经理')

e = E('test',10000,1000)
e.introduction()

'''
# 6、编写游戏相关类：
# 1). 怪物类：当前生命值，原始生命值，当前位置，原始位置，攻击力，防御力，移动行为，攻击英雄行为，逃跑行为
# 2). 英雄类：角色名称，等级，经验，当前生命值，原始生命值，当前位置，原始位置，移动行为，攻击怪物行为
# 3）游戏类：将英雄和怪物传入到游戏类中，进行简单的攻击过程
# 抽出父类，对以上编写的类进行实例化，并且赋值然后调用他们的方法

'''
class Base:
    def __init__(self):
        self.hp = ""
        self.attack = " "

class Monster(Base):

    def __init__(self):
        super().__init__()
        self.defense = ""

class Hero(Base):
    def __init__(self):
        super().__init__()
        self.name = 'hero'

class Game:
    def __init__(self):
        self.hero = Hero()
        self.monster = Monster()

    def interactive(self):
        print('{}杀死{}'.format(self.hero,self.monster))
        
'''
# 扩展，选做：
# 猜拳游戏。请判断哪些可以使用继承关系创建类
# * 玩家(Player)和机器人(Robot)比赛猜拳，1.石头  2.剪刀   3.布
# * 裁判(Judge)判定输赢，并进行加分和减分
# * 三次为一局，询问玩家是否继续比赛，如果继续重新计分

'''
class Player:
    def __init__(self,name):
        self.name = name

    def guess(self,index):
        res = self.__guess(index)
        print('玩家出拳{}'.format(res))
        return index

    def __guess(self,index):
        if index == 1:
            return '石头'
        elif index == 2:
            return '剪刀'
        elif index == 3:
            return '布'
        else:
            raise ValueError('请输入 1 2 3 ')
import random
class Robot:
    def __init__(self):
        self.name = 'robot'
    def guess(self):
        index = random.randint(1,3)
        res = self.__guess(index)
        print('机器人出拳{}'.format(res))
        return index
    def __guess(self,index):
        if index == 1:
            return '石头'
        elif index == 2:
            return '剪刀'
        elif index == 3:
            return '布'
        else:
            raise ValueError('请输入 1 2 3 ')
class Judge:
    def __init__(self):
        self.robot = Robot()
        self.player = Player('jack')
        self.score = 0

    def play(self):
        i = 0
        while i < 3:
            p_index = int(input('请猜拳: '))

            r_index = self.robot.guess()
            self.player.guess(p_index)
            if p_index == r_index:
                print('平分')

            if p_index == 1:
                if r_index == 2:
                    self.win()
                if r_index == 3:
                    self.lose()
            if p_index == 2:
                if r_index == 1:
                    self.lose()
                if r_index == 3:
                    self.win()

            if p_index == 3:
                if r_index == 1:
                    self.win()
                if r_index == 3:
                    self.lose()

            i+=1
        print('玩家分数 {}'.format(self.score))

    def win(self):
        print('玩家赢')
        self.score += 1
    def lose(self):
        print('玩家输')
        self.score -= 1

j = Judge()
j.play()
'''

# 选做题：
# 编写游戏相关类：
# 1). 怪物类：当前生命值，原始生命值，当前位置，原始位置，攻击力，防御力，移动行为，攻击英雄行为，逃跑行为
# 2.) 英雄类：角色名称，等级，经验，当前生命值，原始生命值，当前位置，原始位置，移动行为，攻击怪物行为
# 对以上编写的类进行实例化，并且赋值然后调用他们的方法
# 后期要求：
# 根据上诉需求，从所有的怪物类中找出冗余代码，抽象出一个父类。
# ➢    添加一个英雄父类，并继续添加几个角色。
# ➢    添加一个物品父类，装备、药品都继承自此类。
# ➢    修改游戏，使用多态完善怪物、英雄的攻击。

'''
class Pill:
    def __init__(self,money):
        self.money = money

class MagicPill(Pill):
    pass

class HpPill(Pill):
    pass

class Base:
    def __init__(self):
        self.hp = ""
        self.attack = " "

class Monster(Base):

    def __init__(self):
        super().__init__()
        self.defense = ""

class Hero(Base):
    def __init__(self):
        super().__init__()
        self.name = 'hero'
        self.pill = []

class Magic(Hero):
    def __init__(self):
        super().__init__()
        self.pill = MagicPill(10)

class Warrior(Hero):
    def __init__(self):
        super().__init__()
        self.pill = HpPill(20)

class Pastor(Hero):
    pass

class Game:
    def __init__(self):
        self.hero = Warrior()
        self.monster = Monster()

    def interactive(self):
        print('{}杀死{}'.format(self.hero,self.monster))
        
'''

