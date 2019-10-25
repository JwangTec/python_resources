'''
while语句实现 九九乘法表
'''
i = 1

while i <=9:
    j = 1
    xx =""
    while j <= i:
        xx += ("{0:d} * {1:d} = {2:2d}  |  ".format(i,j,i * j))
        j += 1
    print(xx)
    i += 1

'''
while实现 倒九九乘法表
'''
i = 1

while i <= 9:
    j = 9
    xx =""
    while j >= i:
        xx += ("{0:d} * {1:d} = {2:2d}  |  ".format(i,j,i * j))
        j -= 1
    print(xx)
    i += 1
'''
    1   
   2 3 
  4 5 6
 7 8 9 0
 
 分拆整个：先输出空格，再输出数字
'''
space_num = n - 1
i = 1
n = 4
while space_num >= 0:
    string = (" "*space_num)
    j = 0
    while (n - space_num) > j:
        string += str(i % 10) + " "
        i += 1
        j += 1
    print(string)
    space_num -= 1
'''
*****
****
***
**
*
'''

i = 1
while i < 6:
    string = ("*" * i)
    i += 1
    print(string)

'''
*
**
***
****
*****
'''
# i = 1
# num = 6
# while i < 6:
#     string = ("*" * num)
#     i += 1
#     num = num - 1
#     print(string)


'''
******
 *****
  ****
   ***
    **
     *
'''
# lines = 6
# start_num = 6
# j = lines
# while j > 0:
#     space_num = lines - start_num
#
#     print(" " * space_num + "*" * start_num)
#     start_num -= 1
#     j -= 1

'''
等差数列公式：An = A1 + （n - 1）* d

    1
   111
  11111
 1111111
  11111
   111
    1

'''
import  math

# space_num = 3
# while space_num > -4:
#     print(" " * abs(space_num) + "*" * abs(abs(2 * space_num) - 7))
#     space_num = space_num - 1

# n = 7
# mid = n // 2 + 1 #中间那一排
# i = 1
# while n > 0:
#     space_num = abs(mid-i) #3
#     base_num = mid-space_num #1
#     star_num = base_num*2-1
#     print(' '*space_num + "*"*star_num)
#     i += 1
#     n -= 1





