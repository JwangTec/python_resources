
'''
练习：根据课堂情况可用作课堂练习或者课后练习
1、判定一个输入的整数是否为偶数
'''
# num = int(input("请输入一个整数："))
# if num % 2 == 0:
#     print("输入的{0}为偶数".format(num))
# print("输入的%d不是偶数" %num)
'''
2、验证自己是否成年(18岁及以上属于成年)
'''
# age = int(input("你的年龄是："))
# if age >= 18:
#     print("你已经成年！")
# else:
#     print("你还未成年！")
'''
3、闰年问题（输入一个年份，判断是否为闰年）
能被4整除 不能被100整除
或者能被400整除
'''
# year = int(input("请输入一个年份："))
# if (year % 4 == 0 and year % 100) or (year % 400 == 0):    #判断闰年，不能整除则可以使用 year % 2 若符合则结果为0（False）
#     print("输入的年份为闰年")
# else:
#     print("输入的年份为平年")
'''
4、小明身高1.75，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
（1）低于18.5：过轻
（2）18.5-25以下：正常
（3）25-28以下：过重
（4）28-32：肥胖
（5）高于32：严重肥胖

'''
# height = 1.75
# weight = 80
# bmi_ming = weight / (height ** 2)
# print("小明的BMI指数是：%.2f" %bmi_ming)
# if bmi_ming <= 18.5:
#     print("过轻")
# elif bmi_ming <= 25:
#     print("正常")
# elif bmi_ming <= 28:
#     print("过重")
# elif bmi_ming <= 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

'''
5、购买车票，输入身高，判定1.2m以下输出购买儿童票；其他输出成人票
'''
# ticket = float(input("请输入身高："))
# if ticket <= 1.2:
#     print("请购买儿童票")
# else:
#     print("请购买成人票")
'''
6、输入温度，查看温度适宜问题（15度以下寒冷，15-29度舒适，30度及以上炎热)
'''
# temp = int(input("请输入当前温度："))
# if temp > 30:
#     print("炎热")
# elif temp > 15:
#     print("舒适")
# else:
#     print("寒冷")
'''
7、输入年龄，验证该年龄是否成年(18岁及以上属于成年)
'''
# age = int(input("你的年龄是："))
# if age >= 18:
#     print("你已经成年！")
# else:
#     print("你还未成年！")
'''
8、今天老板找我到办公室，说要调整薪资，输入老板说的薪资，输出我此刻的心情（条件和心情自由设定）
'''
# salary = int(input("老板说的薪资是："))
# if salary > 5000:
#     print("还可以")
# elif salary > 9000:
#     print("老板吃错药了")
# elif salary > 12000:
#     print("老板要炒我鱿鱼了")
'''
# 9、输入一个成绩，如果考试成绩大于 90 分，则奖励一个 IPHONE 8S ，如果成绩介于 70 分至 90 分之间，则奖励一个小米，否则罚做 500 个俯卧撑。
'''
# score = int(input("请输入成绩："))
# if score > 90:
#     print("奖励 IPHONE 8S")
# elif score > 70:
#     print("奖励一个小米")
# else:
#     print("罚500俯卧撑")
'''
10、在游乐场中，门票全票价位10美元
4岁以下免费；
4~18岁收费3美元；
18岁（含）以上收费10美元。
对于65岁（含）以上的老人，可以半价（即5美元）购买门票，输入年龄，查看需要多钱购买门票
'''
# age = int(input("请输入你的年龄： "))
# if age >= 65:
#     print("半票：5美元")
# elif age >= 18:
#     print("全票：10美元")
# elif age >= 4:
#     print("3美元")
# else:
#     print("免费")

#提升：
'''
1、某单位马上要加工资，增加金额取决于工龄和现工资两个因素：
对于工龄大于等于20年的，如果现工资高于2000，加200元，否则加180元；
对于工龄小于20年的，如果现工资高于1500，加150元，否则加120元。工龄和现工资从键盘输入，编程求出一个员工加工资后的工资。
'''
# salary = int(input("你现在的工资为："))
# work_age = int(input("你的工龄为："))
# if work_age >= 20:
#     if salary >= 2000:
#         salary = salary + 200
#     else:
#         salary = salary + 180
# else:
#     if salary >= 1500:
#         salary = salary + 150
#     else:
#         salary = salary + 120
# print("你加工资后的工资为： {0}".format(salary))

'''
2、请写1个ATM程序.定义1个变量,用来存储该ATM机器中剩余的金额.
1)接收用户输入取款金额.由于ATM机器只支持100的票子.
2)如果用户输入的取款金额不是100的倍数的话.则打印 "对不起,本机器无法提供输入的面额"
3)如果用户输入的取款金额大于了ATM的剩余金额.则打印 "对不起,余额不足."
4)如果用户输入的取款金额是100的倍数,并且小于等于ATM的剩余金额就打印."正在出钞,请从出钞口拿钱.ATM机器剩余xx元
'''
# money_sum = 2500
# money_draw = int(input("请输入你的取款金额:\n"))
# if (money_draw % 100) != 0:
#     print("对不起,本机器无法提供输入的面额")
# elif money_draw > money_sum:
#     print("对不起,余额不足.")
# else:
#     money_sum = money_sum - money_draw
#     print("正在出钞,请从出钞口拿钱.ATM机器剩余%d元" %money_sum)

# 扩展内容：
'''
# 输入一个数，判定该数是否为质数
'''
# def is_peime(num):           #判断是否为质数
#     i = 2
#     flag = True
#     while num > i:           #循环条件
#         if not num % i:      #质数判断，若为真（不是质数）则执行判断语句
#             flag = False
#             break            #符合该条件则直接跳出循环
#         i += 1
#     return flag
#
# num1 = int(input("请输入一个大于1的整数： "))    #输出所有符合条件的质数
# while num1 > 0:
#     if is_peime(num1):      #调用质数函数
#         print(num1)
#     num1 -= 1


# xx = 1
# while xx < num:
#     xx += 1
#     if num % xx == 0:
#         print("该数不是质数")
#         break
#     else:
#         print("%d是质数" % num)
#         break


'''
# 1、求 100-200以内同时能被7、8整除的数
'''
# num = 101
# while 100< num < 200:
#     if (num % 7 == 0) and (num % 8 == 0):
#         print(num)
#     num += 1

'''   
# 2、求 1-100以内所有含6的数
'''
# num = 1
# while num < 101:
#     if num % 10 == 6:
#         print(num)
#     num += 1

'''
# 3、使用while和if  ，实现求100以内，个位数和十位数相等的两位数
'''
# num = 1
# while num < 101:
#     if (num % 10) == (num // 10):
#         print(num)
#     num += 1

#基础提升
'''
# 1、求 0 -1 + 2 - 3 + 4 - 5 + 6 -7.... + 100
'''

# num = 0
# sum1 = 0
# while num < 101:
#     if num % 2 == 0:
#         sum1 = sum1 + num
#     sum1 = sum1 - num
#     num += 1
# print(sum1)

'''
2、Chuckie Lucky赢了100W美元，
他把它存入一个每年盈利8%的账户。
在每年的最后一天，Chuckie取出10W美元。
编写一个程序，计算需要多少年Chuckie就会清空他的账户。
'''
# money_sum = 1000000
# age = 0
# while True:
#     if money_sum > 0:
#         money_sum = money_sum * (1 + 0.08) - 100000
#         age = age + 1
#     else:
#         break
# print(age)

# 循环退出练习题：
'''
# 1、银行登录案例
'''
# num = 1
# card = "aa"
# pw2 = 123
# card1 = input("请输入账号：")
# if card1 == card:
#     while True:
#         pw1 = input("第{}次输入密码：".format(num))
#         pw1 = int(pw1)
#         if pw1 == pw2 :
#             print("账号密码正确")
#             break
#         num += 1
#         if num > 3:
#             print("密码错误三次")
#             break
# else:
#     print("账号错误")

'''
# 2、输入班级学生语文成绩，求总成绩和平均成绩 。班级人数从键盘输入
'''
# num1 = int(input("班级总人数是： "))
# num = 1
# ch = 0
# while num <= num1:
#     score = int(input("请输入第{}个学生的语文成绩：".format(num)))
#     ch = score + ch
#     num += 1
# everage = ch / (num - 1)
# print("总成绩为：{0},平均成绩为：{1}".format(ch, everage))

'''
# 3、循环输入7天温度，求平均温度
'''
# num = 1
# c = 0
# while num < 8:
#     xx = int(input("请输入第{}天的温度：".format(num)))
#     c = c + xx
#     num += 1
# aveg = xx / 7
# print(aveg)
'''
# 4、依次输入几个数据，直到0作为输入的结束， 然后求出输入的这些数据的总和及平均值（0不算次数）；
'''
# num = 0
# score = 0
# while True:
#     xx = int(input("依次输入第{}个数字：".format(num)))
#     score = score + xx
#     num += 1
#     if xx == 0:
#         break
# avg = score / (num - 1)
# print("总和为：{0},平均值为：{1}".format(score,avg))
'''
# 5、求1000-5000之间，各位数字之和为5的所有整数，打印输出（例如整数2003的各位数字之和为2+0+0+3，等于5）
'''
# num = 1000
# num1 = 0
# num2 = 0
# num3 = 0
# num4 = 0
# while num < 5000:
#     num1 = num % 10
#     num2 = num // 10 % 10
#     num3  = num // 100 % 10
#     num4 = num // 1000 % 10
#     num5 = num4 + num1 + num2 + num3
#     if num5 == 5:
#         print(num)
#     num += 1
#
#
# 提升：
'''
# 1、从键盘输入10个数，求出最大数
'''
num = 1
max_num = int(input("请依次输入第{}个数：".format(num)))    #初始化最大值，防止输入的数为负数，若比较大小都需要初始化比较值。

while num < 10:
    num += 1
    num1 = int(input("请依次输入第{}个数：".format(num)))
    if num1 > max_num:
        max_num = num1
print(max_num)

'''
# 2、输入一个五位以内的数，求每位数字之和
'''

# num = input("请输入一个五位以内的数： ")
# num2 = 0
# num2 = int(num)
# num1 = len(num)
# sum_num = 0
# if num1  == 5:
#     sum_num = ( num2 % 10 ) + (num2 // 10 % 10) + (num2 // 100 % 10) + (num2 // 1000 % 10) + (num2 // 10000 % 10)
# elif num1  == 4:
#     sum_num = (num2 % 10) + (num2 // 10 % 10) + (num2 // 100 % 10) + (num2 // 1000 % 10)
# elif num1 == 3:
#     sum_num = (num2 % 10) + (num2 // 10 % 10) + (num2 // 100 % 10)
# elif num1 == 2:
#     sum_num = (num2 % 10) + (num2 // 10 % 10)
# else:
#     sum_num = num2
# print(sum_num)

'''
# 3、从键盘输入两个正整数，输出这个范围内的所有偶数： 如：输入 3 和9， 输出4 6 8
'''
# num1 = int(input("请输入第一个正整数："))
# num2 = int(input("请输入第二个整整数："))
# star_num = 0
# end_num = 0
# xx = ""
# if num1 > num2:
#     star_num = num2
#     end_num = num1
# else:
#     star_num = num1
#     end_num = num2
# in_num = star_num
# while in_num <= end_num:
#     if in_num % 2 == 0:
#         xx += str(in_num)+" "
#     in_num += 1
# print(xx)

'''
# 4、从键盘输入一个正整数x，打印输出从0开始的连续n个偶数，如 x = 5,输出 0 2 4 6 8
'''
# num = int(input("请输入一个正整数： "))
# star_j = -2
# end_d = 1
# xx = ""
# while end_d <= num:
#     star_j = star_j + 2
#     xx += str(star_j)+ " "
#     end_d += 1
# print(xx)

'''
# 5、使用循环完成猜数字游戏，确定一个1-100的随机数（整数），提示用户输入数字进入猜的模式；
输入数字后，如果与随机数（整数）相同，提示用户猜成功了；
输入数字后，如果与随机数（整数）不相同，提示用户猜大一点或者小一点；
记录猜的次数，如果猜的次数小于三次，则赞赏，真聪明
如果大于等于3次小于10次，则表示，要加油哦
随机数获取：百度  python3 random 关键字，查询资料获得
'''

# import random
# num2 = 1
# aa = int(random.uniform(1, 100))
# is_aa = True
# while is_aa:
#     bb = int(input("第{}输入你的数字：".format(num2)))
#     if bb == aa:
#         print("恭喜你，猜对了！")
#         if num2 < 3:
#             print("真聪明")
#         elif 3 <= num2 < 10:
#             print("还需加油")
#         else:
#             print("...")
#         is_aa = False
#     else:
#         if bb > aa:
#             print("你的数字太大了")
#         else:
#             print("你的数字太小了")
#     num2 += 1


'''
# 6、打印100-999中不能被7整除又不包含7的数
'''

# star_num = 100
# end_num = 1000
# num = ""
# while star_num < end_num:
#     num1 = star_num % 10
#     num2 = star_num // 10 % 10
#     num3 = star_num // 100
#     if (num1 != 7 and num2 != 7 and num3 != 7) and (star_num % 7 != 0):
#         num = num + str(star_num) + " "
#
#     star_num += 1
# print(num)

