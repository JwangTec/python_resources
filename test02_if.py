'''
控制语句：
if 判断语句，
只接受True/False，只运行判断为真的语句快。
语句快中pass会不执行这一块语句
可以在判断语句中先赋值，再在语句外调用该值
if   else:
if elif else: 满足其中一个条件则执行该条件后直接跳出语句块
'''

# is_plus = True #是否是会员    # 基础判断
# if is_plus:
#     print("恭喜你，会员大大 ")
# elif not is_plus:
#     print("垃圾小号")
# else:
#     print("请充钱")
# print("用薪创造快乐")
#
#
# is_plus = False
#
# price = float(input('price: '))
#
# if is_plus:
#     price = price * 0.7
# else:
#     price = price * 0.95
# print(price)
#
# if is_plus:
#     price = price * 0.7
# print("price: %.2f" %price)
#
# buy_sum = float(input("购买后金额为："))     #折扣计算
#
# if buy_sum > 400:
#     buy_sum = buy_sum * 0.85
#     print(buy_sum)
# else:
#     if buy_sum < 0:
#         print("非法操作")
#     else:
#         buy_sum = buy_sum * 0.95
#         print("实际支付金额：%.2f" %buy_sum)
#
# if buy_sum < 0:
#     print("非法操作")
# else:
#     if buy_sum > 400:
#         buy_sum = buy_sum * 0.85
#     else:
#         buy_sum = buy_sum * 0.95
#     print("实际支付金额：%.2f" % buy_sum)
#
# h = input("请输入你的身高：")
# h = float(n)
#
# if h < 1.2:
#     print("儿童票")
# else:
#     print("成人票")
#
# if buy_sum < 0:
#     print("error")
# else:
#     if buy_sum < 400:
#         buy_sum = buy_sum * 0.95
#     elif 400 >= buy_sum <= 1000:
#         buy_sum = buy_sum * 0.8
#     elif 10000> buy_sum > 1000:
#         buy_sum = buy_sum * 0.5
#     else:
#         buy_sum = buy_sum * 0.2
#     print(buy_sum)
#
#
#
# if buy_sum < 0:
#     print("error")
# else:
#     if buy_sum < 400:
#         buy_sum = buy_sum * 0.95
#     elif  buy_sum < 1000:
#         buy_sum = buy_sum * 0.8
#     elif 10000> buy_sum:
#         buy_sum = buy_sum * 0.5
#     else:
#         buy_sum = buy_sum * 0.2
#     print(buy_sum)
#
# score = float(input("分数： "))     #输入分数并判断其等级
# if score < 0 or score > 100:
#     print("无法判断")
# else:
#     if score >= 90:
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
# if score > 100 or score < 0:
#     print("无法判断")
# elif score >= 90:
#     print("等级为： A")
# elif score >= 80:
#     print("等级为： B")
# elif score >= 70:
#     print("等级为： C")
# elif score >= 60:
#     print("等级为： D")
# else:
#     print("等级为： F")

