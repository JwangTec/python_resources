# 1、书写一个程序，用户输入一个数字（圆的半径）要求输出该圆的半径、周长和面积，输出格式如下：
# 	 该圆半径为：xx
# 	 该圆周长为：xx
# 	 该圆面积为：xx

import math
'''
r = float(input("请输入圆的半径：" ))
c = 2 * math.pi * r
e = math.pi * r * r
print("该圆的半径为：{0}\n该圆的周长为：{1:.5f}\n该圆的面积为：{2:.5f}\n".format(r, c, e))
'''
# 2、解释以下程序的打印结果
# print(1 + 10 * 2 / 2 - 5)   运算符优先级：存在除法（/）运算符，结果显示为浮点数，6.0
# print(3.0 / 5)              浮点数/整数 = 浮点数
# print(3.0 // 5)             向下取整 且除数是浮点数 结果为0.0
# print('a' * 10)             对字符串使用* 相当于连接符，对"a"重复10次
# print(True + 3)             True 为 1 ， 1+3 =4
# print(False + 3)            False为0， 0+3=3
# print('hello' > 'world')    比较两个字符串的Ascil码
# print('h' > 1)              字符串无法与整型相比较 会报错，类型不同

# 3、说出以下正确的定义变量有哪些？
# ab = 10 true
# *a = 20 false
# _a = 20 true
# pass = 1 false
# global = 2 false
# 1a = "hello" false
# b = '''world''' true
# python = ""hi"" True

# 4. 定义一个变量。用来存储我卡上有100块钱，到银行存了1000块钱，打印输出现在我卡上多少钱

# money_now = int(input("现在存储卡上余额为："))
# save = int(input("现在到银行存款："))
'''
money_now = 100
save = 1000
print("存储卡上余额：{0}, 现存款：{1}, 存款后卡上余额为：{2}".format(money_now, save, money_now+save))
'''
# 5、班费有199块钱，买了30支笔，每支笔2.5元，买了5个杯子，5元一个，打印输出班费还剩多少钱？
'''
Class_sum_money = 199
Buy_pen = 30 * 2.5
Buy_cup = 5 * 5
print("班费还剩：%.2f" %(Class_sum_money-Buy_cup-Buy_pen))
'''

# 6. 使用运算符，求19的个位打印输出；求29的十位数字打印输出；189的每位数字输出；

'''
print("19的个位为：%d" %(19%10))
print("29的十位数是： {0}".format(29//10))
print("189的个位数是：{0}, 十位数是： {1}, 百位数是： {2}".format(189%10, 189//10, 189//100))
'''

# 7 、已知一个学生两科成绩：语文90；英语66；求该学生总成绩和平均成绩
'''
chinese = 90
english = 66
total_course = chinese + english
everage_course = total_course / 2
print("该学生的总成绩为： {0}, 平均成绩为： {1}".format(total_course, everage_course))
'''
# 8、已知正方形边长为4，求正方形周长和面积
'''
square_length = 4
square_c = square_length * 4
square_e = square_length ** 2
print("边长为{0}的正方形周长为{1},面积为{2}".format(square_length, square_c, square_e))
'''
# 9、已知一个圆半径为3.5，声明一个变量名为radius存储该圆半径，要求输出该圆的半径、周长和面积
'''
radius = 3.5
cir_girth = radius * math.pi * 2
cir_eare = math.pi * radius ** 2
print("该圆的半径为： {0}\n该圆的周长为： {1}\n该圆的面积为：{2}".format(radius, cir_girth, cir_eare))
'''

print(189//10%10)