'''
hash:相当于身份证号，长度一样，具有唯一性 散列 运行速度快
实现hash算法：md5 sha1 sha256    无法解密  应用：磁力链接 dict：中键使用的hash值，
可hash类型：不可更改的：例如：数字，字符，字符串，元祖  比较消耗内存
不可hash（散列）类型：list
'''


#判断某个字符是否在一个字典中使用in时 判断的是键 而不是值或者两者
#测试效率
#............
def gen_list(n):
    list1 = (i for i in range(n))
    return list1

def gen_dict(n):
    dict1 = {i:i for i in range(n)}
    return dict.fromkeys(dict1)

def gen_set(n):
    set1 = set(i for i in range(n))
    return set1


import random

def gen_random_list(n = 10):     #生成n或者默认10个1-10000的随机数
    list_random = [random.randint(0,10000) for i in range(n)]
    return list_random

import time
def dec(fun):
    def res(*args, **kwargs):
        print('-------- %s | 长度  %d-------------' % (type(args[0]),len(args[0])))
        start = time.perf_counter()
        a = fun(*args, **kwargs)
        print('本次算法消耗的时间为 %s' % ((time.perf_counter() - start)*10**5))
        print('******************')
        return a

    return res


@dec
def test_in(test_l):         #判断生成的随机数是否在test_l中
    list1_random = gen_random_list()
    for i in list1_random:
        if i in test_l:    #比较 如果是字典，则判断的是键所对应的
            pass

def test():    #调用set,dict,list函数分别依次生成有序的100，100，10000个数的相关
    x = list()
    for list_gen in [gen_list, gen_dict, gen_set]:
        for i in range(2,5):
            x.append(list_gen(10**i))

    for j in x:     #循环x中的元素
        test_in(j)  #调用随机数函数判断j是否在x中

test()


