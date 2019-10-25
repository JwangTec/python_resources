#
# __doc__ = """
#
# 作业：
# 1、请写一个函数，判定一个三位数字是否为水仙花
''''
def is_daffodil(num):
    num1 = num % 10
    num2 = num // 10 % 10
    num3 = num // 100
    total_square = num1**2 + num2**2 + num3**2
    if total_square == num:
        return "该数是水仙花"
    else:
        return "该数不是水仙花"

print(is_daffodil(555))

'''

# 2、不使用自带函数，写一个函数，用于返回一个数的绝对值
'''
def absolute_value(num):
    if num >=0:
        return num
    else:
        return (-num)
print(absolute_value(-20))
'''
# 3、两数值的谐均值可以这样计算：
#  首先对两数值的倒数取平均值，最后再取倒数。
# 编写一个带有两个小数参数的函数，返回两个参数的谐均值。
'''
def harmonic_mean(num1, num2):
    reciprocal_num1 = num1**(-1)
    reciprocal_num2 = num2**(-1)
    average_num12 = (reciprocal_num1 + reciprocal_num2) / 2
    reciprocal_avg = average_num12**(-1)
    return reciprocal_avg

print(harmonic_mean(2.5,4.6))
'''
# 提升：# 4、写一个函数，返回输入整数（大于0小于10000）的每位数的数字之和。
'''
def total_number(num):
    num_one = num % 10
    num_ten = num // 10 % 10
    num_hundred = num // 100 % 10
    num_thousand = num // 1000 % 10
    total_num = num_one + num_ten + num_hundred + num_thousand
    return  total_num
print(total_number(12))
'''
# 例如：1234    1+2+3+4 = 10
#
# 5、写一个函数，用来求三个数中的最大数
'''
def max_three(a, b ,c):
    max_num = a
    if max_num < b:
        max_num = b
    if max_num < c:
        max_num = c
    return  max_num
print(max_three(20,5,10))
'''
# 6、输入某年某月某日，写一个函数，判断这一天是这一年的第几天？

# # 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# # 特殊情况，闰年且输入月份大于3时需考虑多加一天。
'''
def is_day(year,month,day):
    sum_day = 0
    month_num = 1
    while month_num < month:
        if month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
            one_day = 30

        elif month_num == 2:
            if ( year % 100 == 0 and year % 400 ==0)or  year % 4 ==0:
                one_day = 29

            else:
                one_day = 28

        else:
            one_day = 31
        month_num += 1
        sum_day += one_day

    sum_day = sum_day + day

    return sum_day

print(is_day(2019,2,2))

'''

# 扩展：
# 1、编写一个函数，传入一个数，判定是否为质数
'''
def is_prime(num):
    string_num = ""
    xx = num - 1
    while xx > 1:
        if num % xx == 0:
            num_str = str(xx)
            string_num += num_str
        xx -= 1
    if len(string_num) == 0:
        yy = "该数为质数"
    else:
        yy = "该数不是质数"

    return yy



print(is_prime(7))
'''
# 2、书写一个简洁版的取钱和存钱的功能
# 1）登录函数，传入用户名和密码进行登录；
# 2）登录成功后，可以反复存钱和取钱，直到用户选择退出



def load_user(passwoard,user_name):                        #登陆确认
    if passwoard == 2019 and user_name == "wangqi":
        return 1

def deposit(balance,money):                  #存钱
    balance += money
    return balance
def withbra(balance, money):               #取钱
    balance += money
    return balance

def bank_load():
    is_num = True
    while is_num:
        user_load = input("请输入你的账号：")
        pass_word = int(input("请输入你的密码："))
        if load_user(pass_word, user_load):                #账号判断
            is_num = False
        else:
            is_num = True

def bank_deposit():
    bank_load()
    is_money = True
    while is_money:                                     #存取款循环
        balance = 200
        is_deposit = int(input("取款请按0，存款请按1\n"))
        if is_deposit:
            money = int(input("请输入存款金额："))
            balance = deposit(balance,money)
        else:
            money = int(input("请输入取款金额："))
            balance = withbra(balance,money)
        print("你现在的余额为：%d" %balance)
        is_exit = int(input("退出请按 0，继续请按 1\n"))           #循环结束或继续判断
        if is_exit:
            is_money = True
        else:
            is_money = False


bank_deposit()
