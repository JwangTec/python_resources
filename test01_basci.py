# import keyword
# import math
# import os
# print("hello world!")   #   使用CPU进行标准输出到屏幕
#
# print(type('world'))
#
# print(keyword.kwlist)
# print(1)
# print(2+3)
# print(1.0)
# print(2.5+2.5)
# print    ('hello')
# print('hello' + 'world')
# print('hello' + "world")
# print(1+2.0)
# print(type(1))
# print(type(1.0))
'''
print(bin(12345))

print(0b11000000111001)

'''
# aa =12344
# bb = 12345.0
# print("%5d, %.1f" %(aa, bb))
# cc ="asdf"
# print("%d, %e" %(aa, aa))


'''
"十六进制转换函数"

aa = int(input("请输入一个十进制整数num："))
def XD_exchange(num):
    print("%d 的 十六进制是 %x " %(num, num))
    print("%d 的 十六进制是 %x " %(num, num)) 

XD_exchange(aa)

'''
# aa = int(input("请输入一个十进制数整数num："))
# print("%d 的 十六进制是 %x " %(aa, aa))
# aa = int(input("请输入一个十进制数整数num："))
# print("{0} 的 十六进制是 {1} ".format(aa, aa))


'''
变量
'''
'''
def X_exchange(aa):
    print("%d 的 十六进制是 %x " %(aa, aa))
def E_exchange(bb):
    print("%d 的 科学计数法是 %e " %(bb, bb))
def B_exchange(cc):
    print("{0} 的 二进制是 {1}".format(cc, bin(cc)))
num = input("请确认需要输入的整数：")
if  num.isdigit():
     num1 = int(num)
     X_exchange(num1)
     E_exchange(num1)
     B_exchange(num1)
else:
    num2 = len(num)
    print("{0} 是一个字符串，其占用字节数为{1}".format(num,num2))

'''

# name = "超级咸蛋超人"
#
# kill = 99999999.55555555555
#
# print("%s 一拳伤害 %d, 精确到小数点后9位为：%.9f"%(name, kill,kill))


'''
format
'''


'''
运算符： + - * / %
向下取整： // 
向上取整 ： 调用函数math， math.ceil()
取模：%
幂运算： **  2**3 = 2^3
比较符：> <  >=  <= != == (判断的是对象的值)  python可以使用连续判断
布尔代数：二进制位运算：| >> << & ^ 
not 0 = true  not 4 = false  除0全是true  字符串空也为false 非空为true             注意：False 首字母大写
逻辑运算符：and  in  or not is(对象是否相同：地址等)
惰性原则：print((1 < 2) or (x > 6))  true

python优化机制
'''

# aa = [10,1,1,2,2,3,3,4,4]
# num = len(aa)
# i = 0
# if i in range(num):
#     for j in range(i, num):
#         if aa[i] != aa[j]:
#             dd = aa[i]
#
# print(dd)


'''
复习：
进制换算
代码运行规则：自上而下，从右向左
下滑波浪线：错误提示，红色表示严重错误
简易优先级：数学符号优先级
系统默认0或者空为False
^ & << >> ~ | ：如果为数字 则进行二进制运算
制表符：TAB键与空格
'''


# n1 = [123, 0x456, 0XEF,0b111]
# print(n1)
#
# n2 = int(input("输入整数： "))
# print("%d 的16进制是 %X " %(n2,n2))
#
# print("{0} 的 二进制 是{1}".format(n2, bin(n2)))

# x = 1 - 4**2 + 10 // 1.0
# print(x)

# aa = [not 8, not 0, not "", 'c' in "aa", "c" is 'c', 8>9 or 7<9, 10 > 2 and 10 < 2]
# print(aa)

# print(10 | 11)
# 1 0 1 0
# 1 0 1 1
#=========
# 1 0 1 1    10 | 11
# 0 0 0 1    10 ^ 11
# 1 0 1 0    10 & 11

















    



