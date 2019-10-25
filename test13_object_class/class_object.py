'''

http://www.cnblogs.com/linhaifeng/articles/7341318.html
https://www.cnblogs.com/wj-1314/p/8734839.html

类即类别、种类，是面向对象设计最重要的概念，对象是特征与技能的结
合体，而类则是一系列对象相似的特征与技能的结合体

那么问题来了，先有的一个个具体存在的对象（比如一个具体存在的人），
还是先有的人类这个概念，这个问题需要分两种情况去看

在现实世界中：先有对象，再有类
世界上肯定是先出现各种各样的实际存在的物体，然后随着人类文明的发展，
人类站在不同的角度总结出了不同的种类，如人类、动物类、植物类等概念
也就说，对象是具体的存在，而类仅仅只是一个概念，并不真实存在
对象1：李坦克
    特征:
        学校=oldboy
        姓名=李坦克
        性别=男
        年龄=18
    技能：
        学习
        吃饭
        睡觉

对象2：王大炮
    特征:
        学校=oldboy
        姓名=王大炮
        性别=女
        年龄=38
    技能：
        学习
        吃饭
        睡觉
现实中的老男孩学生类
    相似的特征:
        学校=oldboy
    相似的技能：
        学习
        吃饭
        睡觉

在程序中：务必保证先定义类，后产生对象
这与函数的使用是类似的，先定义函数，后调用函数，类也是一样的，在程序中需要先定义类，后调用类
不一样的是，调用函数会执行函数体代码返回的是函数体执行的结果，而调用类会产生对象，返回的是对象

按照上述步骤，我们来定义一个类（我们站在老男孩学校的角度去看，在座的各位都是学生）
'''

#程序中定义类：保证先定义类再使用（产生对象）1.在程序中特征用变量标识，技能用函数标识 2.因而类中最常见的无非是：变量和函数的定义
class Iboyoldschool:
    school = 'oldboy'
    def learn(self):
        print('learning function')

    def eat(self):
        print('eating function')

    def sleep(self):
        print('sleeping function')
'''
#注意：
  1.类中可以有任意python代码，这些代码在类定义阶段便会执行
  2.因而会产生新的名称空间，用来存放类的变量名与函数名，可以通过Iboyoldschool.__dict__查看
  3.对于经典类来说我们可以通过该字典操作类名称空间的名字（新式类有限制），但python为我们提供专门的.语法
  4.点是访问属性的语法，类中定义的名字，都是类的属性
'''

print(Iboyoldschool.__dict__)

#程序中类的用法：1.  . :专门用来访问属性，其本质是操作__dict__
Iboyoldschool.school  # --> Iboyoldschool.__dict__['school']
Iboyoldschool.x = 1   # --> Iboyoldschool.__dict__['x'] = 1
del Iboyoldschool.x   # -->Iboyoldschool.__dict__.pop('x')

#程序中的对象：调用类，或成为类的实例化，得到对象
s1 = Iboyoldschool()
s2 = Iboyoldschool()

#如此，s1、s2都一样了，而这三者除了相似的属性之外还各种不同的属性，这就用到了__init__
#注意：该方法是在对象产生之后才会执行，只用来为对象进行初始化操作，可以有任意代码，但一定不能有返回值

class Iboyoldschool1:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

s3 = Iboyoldschool1('aa','男',12) #过程：先调用类产生空对象s3，然后调用Iboyoldschool1.__init__(s1,'aa','男',12)
s4=Iboyoldschool1('王大炮','女',38)

#程序中对象的用法
#执行__init__,s1.name='牛榴弹'，很明显也会产生对象的名称空间
print(s3.__dict__)
s3.name #s3.__dict__['name']
s3.name = 'aa' # --> s3.__dict__['name'] = 'aa'

#python为类内置的特殊属性
'''
类名.__name__# 类的名字(字符串)
类名.__doc__# 类的文档字符串
类名.__base__# 类的第一个父类(在讲继承时会讲)
类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
类名.__dict__# 类的字典属性
类名.__module__# 类定义所在的模块
类名.__class__# 实例对应的类(仅新式类中)
'''

#类的两种属性：数据属性和函数属性

#类的数据属性是所有对象共享的,id都一样
print(id(Iboyoldschool.school))
print(id(s1.school))
print(id(s2.school))
'''
4377347328
4377347328
4377347328
'''
#类的函数属性是绑定给对象使用的,obj.method称为绑定方法,内存地址都不一样
#ps:id是python的实现机制,并不能真实反映内存地址,如果有内存地址,还是以内存地址为准
print(Iboyoldschool.learn)
print(s1.learn)
print(s2.learn)
'''
<function OldboyStudent.learn at 0x1021329d8>
<bound method OldboyStudent.learn of <__main__.OldboyStudent object at 0x1021466d8>>
<bound method OldboyStudent.learn of <__main__.OldboyStudent object at 0x102146710>>
<bound method OldboyStudent.learn of <__main__.OldboyStudent object at 0x102146748>>
'''


#在obj.name会先从obj自己的名称空间里找name，找不到则去类中找，类也找不到就找父类...最后都找不到就抛出异常


#改写：绑定到对象的方法特殊之处在于，绑定给谁就由谁来调用，谁来调用，
# 就会将‘谁’本身当做第一个参数传给方法，即自动传值（方法__init__也是一样的道理）
# 绑定到对象的方法的这种自动传值的特征，决定了在类中定义的函数
# 都要默认写一个参数self，self可以是任意名字，但是约定俗成地写出self。
#改写
class OldboyStudent:
    school='oldboy'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def learn(self):
        print('%s is learning' %self.name) #新增self.name

    def eat(self):
        print('%s is eating' %self.name)

    def sleep(self):
        print('%s is sleeping' %self.name)


s1=OldboyStudent('李坦克','男',18)
#类中定义的函数（没有被任何装饰器装饰的）是类的函数属性，类可以使用，但必须遵循函数的参数规则，有几个参数需要传几个参数
OldboyStudent.learn(s1) #李坦克 is learning

#对象的交互：

#定义英雄锐雯
class Riven:
    camp='Noxus'
    def __init__(self,nickname,
                 aggressivity=54,
                 life_value=414,
                 money=1001,
                 armor=3):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_value=self.aggressivity-enemy.armor
        enemy.life_value-=damage_value
#定义英雄盖论
class Garen:
    camp='Demacia'
    def __init__(self,nickname,
                 aggressivity=58,
                 life_value=455,
                 money=100,
                 armor=10):
        self.nickname=nickname
        self.aggressivity=aggressivity
        self.life_value=life_value
        self.money=money
        self.armor=armor
    def attack(self,enemy):
        damage_value=self.aggressivity-enemy.armor
        enemy.life_value-=damage_value

#定义装备：多兰之剑
class BlackCleaver:
    def __init__(self,price=475,aggrev=9,life_value=100):
        self.price=price
        self.aggrev=aggrev
        self.life_value=life_value
    def update(self,obj):
        obj.money-=self.price #减钱
        obj.aggressivity+=self.aggrev #加攻击
        obj.life_value+=self.life_value #加生命值
    def fire(self,obj): #这是该装备的主动技能,喷火,烧死对方
        obj.life_value-=1000 #假设火烧的攻击力是1000

#测试交互

r1=Riven('草丛伦')
g1=Garen('盖文')
b1=BlackCleaver()

print(r1.aggressivity,r1.life_value,r1.money) #r1的攻击力,生命值,护甲

if r1.money > b1.price:
    r1.b1=b1
    b1.update(r1)


print(r1.aggressivity,r1.life_value,r1.money) #r1的攻击力,生命值,护甲

print(g1.life_value)
r1.attack(g1) #普通攻击
print(g1.life_value)
r1.b1.fire(g1) #用装备攻击
print(g1.life_value) #g1的生命值小于0就死了

##初始化方法

#方式三、为对象初始化自己独有的特征
class People:
    country='China'
    x=1

    def chu_shi_hua(obj, x, y, z): #obj=obj1,x='egon',y=18,z='male'
        obj.name = x
        obj.age = y
        obj.sex = z

    def run(self):
        print('----->', self)

obj1=People()
# print(People.chu_shi_hua)
People.chu_shi_hua(obj1,'egon',18,'male')

obj2=People()
People.chu_shi_hua(obj2,'lxx',38,'female')

obj3=People()
People.chu_shi_hua(obj3,'alex',38,'female')

# 方式四、为对象初始化自己独有的特征
class People:
    country='China'
    x=1

    def __init__(obj, x, y, z): #obj=obj1,x='egon',y=18,z='male'
        obj.name = x
        obj.age = y
        obj.sex = z

    def run(self):
        print('----->', self)

obj4=People('egon',18,'male') #People.__init__(obj1,'egon',18,'male')
obj5=People('lxx',38,'female') #People.__init__(obj2,'lxx',38,'female')
obj6=People('alex',38,'female') #People.__init__(obj3,'alex',38,'female')


# __init__方法
# 强调：
#   1、该方法内可以有任意的python代码
#   2、一定不能有返回值
class People:
    country='China'
    x=1

    def __init__(obj, name, age, sex): #obj=obj1,x='egon',y=18,z='male'
        # if type(name) is not str:
        #     raise TypeError('名字必须是字符串类型')
        obj.name = name
        obj.age = age
        obj.sex = sex


    def run(self):
        print('----->', self)


# obj7=People('egon',18,'male')
obj7=People(3537,18,'male')

# print(obj1.run)
# obj1.run() #People.run(obj1)
# print(People.run)

#### ！！！__init__方法之为对象定制自己独有的特征

