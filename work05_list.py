#
# __doc__ = """
#
# 作业：
# 1、循环录入5个数字，然后按反序输出（将一个数组中的值按逆序重新存放，
# # 例如原来的顺序为：8，6，5，4，1.要求改为：1，4，5，6，8输出；并将数组中的值输出）
'''
list1 = []
i = 4
while i >= 0:
    list1.append(int(input('请输入第%d个数：'%(5-i))))
    i -= 1
list2 = list1[::-1]
print(list2)
'''
# 2、['12','13','33','34']，移除这个数组中包含1的字符串，提示：使用成员运算符in判定是否包含
'''
def test(list1):
    for nums in l:
        for num in nums:       #for循环会在删除一个后直接从下一个开始，所以第二次会出现新列表的第1个元素未在里面，解决办法：倒着循环
            if num == "1":
                list1.remove(nums)
                continue
list2 = ['12','13','33','34']
test(list2)
# 、、、、、、、、、、、、、、、、、、、、、
list1 = ['12','13','33','34']
list2 = []
for i in list1:
    if '1' not in i:
        list2.append(i)
list1 = list2
print(list1)
'''
# 3、找出一个数组中，输出数字小于33的元素 如数组：[11,22,33,1,6,4,88,44] 和数组 ['11','22','33','1','6','4','88','44']

'''
list1 = ['11','22','33','1','6','4','88','44']
list2 = []
mix_num = 33
for i in list1:
    if int(i) < mix_num:
        list2.append(i)

print(list2)

'''
# 4、找出一个列表中，只出现了一次的数字，并且保持原来的次序，例如[1,2,1,3,2,5]结果为[3,5]
'''
list1 = [1,2,1,3,2,5]
n = len(list1)
count = 0
list2 = []
for i in range(n):
    x = i + 1
    for j in range(x,n):
        if list1[i] == list1[j]:
            list2.append(list1[i])
list3 = list(set(list1) - set(list2))
print(list3)

#简化
def test(l):
    res = [i for i in l if l.count(i) == 1]
    return res
'''

# 5、一个列表中，存放多个数字，查找这个列表中的最大值；
'''
import random
list2 = [random.randint(0,1000) for i in range(10)] #随机生成列表
list1 = [1,2,3,34,45,123,67,23,1111]

for i in range(len(list1)):
    max_num = list1[0]
    if max_num <= list1[i]:
        max_num = list1[i]
print(max_num)
'''
# 6、随机产生20个100-200之间的正整数存放到数组中，并求数组中的所有元素最大值、最小值、平均值，然后将各元素的与平均值的差组成一个新列表。
'''
import random
list1 = []
list2 = []
for i in range(20):
    list1.append(random.randint(100,200))
sum_list1 = 0
for i in range(len(list1)):
    max_num = list1[0]
    min_num = list1[0]
    if max_num <= list1[i]:
        max_num = list1[i]
    if min_num >= list1[i]:
        min_num = list1[i]
    sum_list1 += list1[i]
avge_list1 = sum_list1 / len(list1)
list2.append(max_num)
list2.append(min_num)
list2.append(avge_list1)

print(list2)

'''
# 7、将字符串中的数字去掉，字母转为大写：“0go08o32d”
'''
string_1 = '0go08o32d'
string_2 = ''
list1 = list(string_1)
list2 = []
for i in list1:
    if not str(i).isdigit():
        list2.append(i)
for j in list2:
    string_2 += j
print(string_2.upper())

'''



# 8、给定一个字符串，判断字符串中是否还有png，有就删除它
'''
str_1 = "asadasdasdfpngad"
str_2 = str_1.replace('png','')
print(str_2)

l = s.split("png")
print("".join(l))

'''
# 9、aaabbccccdd输出为3a2b4c2d  #字典解答
'''
str_1 = 'aaabbccccdd'
x1 = str_1.count('a')
x2 = str_1.count('b')
x3 = str_1.count('c')
x4 = str_1.count('d')
str_2 = "%d%s%d%s%d%s%d%s"%(x1,'a',x2,'b',x3,'c',x4,'d')
print(str_2)

def test(words):
    d = dict()
    for word in words:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
    string1 = ""
    for k,v in d.items():
        string1 += '%s%s' %(v,k)
    print(string1)
'''
# 10、写一个函数，计算任意一个身份证号对应的出生年月日和性别
'''
def card_time(string_1):
    year = string_1[6:10]
    month = string_1[10:12]
    day = string_1[12:14]
    if int(string_1[-1]) % 2 == 0:
        sex = '女'
    else:
        sex = '男'
    print('%s年%s月%s日性别%s'%(year,month,day,sex))

card_time('510824199505276535')
'''
# 逻辑题：
# 1、编写一个函数，输入n为偶数时，调用函数求1/2 + 1/4 + ... + 1/n

# # 当输入n为奇数时，调用函数求1/1 + 1/3 + ... + 1/n


# 思考：如何简化为一个函数完成，通用两个功能
#

'''
def f(n):
        if n == 2:
            return (1 / 2)
        if n == 1:
            return 1
        else:
            return 1/n+1/f(n-2)
print(f(3))
'''
# 经典面试题：
# 1、杨辉三角实现：
# # 1
# # 1  1
# # 1  2  1
# # 1  3  3  1
# # 1  4  6  4  1
# # 1  5  10 10 5 1
# # ........
#
'''
def yunhui(n):
    list=[1]              #第一行是特例
    print(list)
    count=1
    for i in range(1,n):
        last=list.copy()
        last.append(0)     #补0
        list.clear()
        for j in range(i+1):
            list.append(last[j-1]+last[j])
        else:
            count+=1
            print(list)
yunhui(10)

def yunhui(n):
    list=[]        #设置一个空列表
    count=1
    for i in range(n):
        cur=[1]
        list.append(cur)     #每一行开头是1，先固定1
        if i==0:                  #第一行属于特殊行
            continue
        last=list[i-1]
        for j in range(i-1):
            cur.append(last[j]+last[j+1])   #上一行的基础上得出
        else:
            cur.append(1)    #末尾追加一个1
            print(cur)
            count+=1
yunhui(6)


def yunhui(n):
    last1 = [1]
    print(last1)
    i = 2
    while i <=n:
        l = []
        for j in range(i):
            if j == 0 or j ==(i -1):
                l.append(1)
            else:
                l.append((last1[j]+last1[j - 1]))
            j += 1
        last1 = l
        print(l)
        i+=1

yunhui(3)
'''
# 2、[1 - 1000],有一个数重复了，只扫描一遍，找出重复数
'''
import random
def random_list(n):       #生成一组只有一个未重复的元素的列表
    list1 = [i for i in range(n)]*2
    list1.remove(random.randint(0,n))
    return list1

def if_not_num(n):  #找到未重复的数
    list2 = random_list(n)
    print(list2)
    a = list2[0]
    for i in range(1,len(list2)):
        a ^= list2[i]         #二进制判断是否未重复
    print(a)


import random
def random_list_one(n):       #生成一组只有一个重复的元素的列表
    list1 = [i for i in range(n)]
    list1 += [random.randint(0,n-1)]
    return list1

def if_num(n):         #判断重复的元素并输出
    list2 = random_list_one(n)
    print(list2)
    for i in list2:
        if list2.count(i) > 1:
            xx = i
    print(xx)

#或者
def if_num1(n):
    list1 = random_list_one(n)
    print(list1)
    s = set()
    num = len(s)
    for i in list1:
        s.add(i)
        if num == len(s):
            print(list1[i])
        else:
            num += 1

'''
# 3、经典面试题：
# 求整型列表（每个元素都是0-9的整数）中最长连续元素子串所组成的最大的数值。
# 测试数据
# [1,3,3,3,4,4,4,4,4,0,0,0,4,4,4,4]，此例中由5个连续的4为最大连续子串，返回结果为44444.
# [1,3,3,3,4,4,4,4,4,0,0,0,0,0,0,5,5,5,5]，返回44444;
# [1,3,3,3,5,5,5,5,5,4,4,4,4,4,0,0,0,0,0,0,4,4,4,4]，返回55555;
#
'''
def find1(l):
    num = l[0] #num练习出现的数字
    max_value = 0#最大数值初始化为0
    counter = 1
    for i in range(1,len(l) - 1):
        if l[i] != num:
            #不等于后面的数 结束counter
            num_string = str(num) * counter
            num_int = int(num_string)
            if num_int > max_value:
                max_value = num_int
            counter = 1
            num = l[i]
        else:
            counter += 1
    return max_value

l = [1,3,3,3,3,3,3,3,3,4,4,4,4,4,0,0,0,0,0,0,5,5,5,5]
print(find1(l))

'''

