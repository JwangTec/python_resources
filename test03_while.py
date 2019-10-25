'''
循环语句：
while：若判断条件为真，循环运行其中的语句块，若为假，运行语句块外语句  注意：每次循环都会执行一次while进行判断
break：停止循环
continu：结束本次循环继续下一次循环

'''

# 测试循环与跳出循环测试：
# is_wh = True
# while is_wh:                                # 每次循环都从while开始
#     score = float(input("分数： "))
#     if score > 100 or score < 0:
#         print("无法判断")
#         is_wh = False                       #或使用 break
#     elif score >= 90:
#         print("等级为： A")
#     elif score >= 80:
#         print("等级为： B")
#     elif score >= 70:
#         print("等级为： C")
#     elif score >= 60:
#         print("等级为： D")
#     else:
#         print("等级为： F")
#
# xx = 1
# num = 0
# while xx < 6:
#     score = float(input("请输入第 %d 科成绩：" %xx))
#     num = num + score
#     xx = xx + 1
# everage = num / 5
# print("总成绩为：{0},平均成绩为：{1}".format(num, everage))
#
# num = 1
# score = 0
# while True:
#     n = input("请输入第{}科成绩: ".format(num))
#     n = int(n)
#     if n > 100 or n < 0:
#         n = input("输入错误，请重新输入第{0}科成绩".format(num))     #print（"输入错误，请重新输入"） continue
#         n = int(n)                                               #使用continu可以结束本次循环
#     score = score + n
#     if num >=5:
#         print("总成绩为：{0},平均成绩为：{1}".format(score, score/num))
#         break
#
#     num += 1



