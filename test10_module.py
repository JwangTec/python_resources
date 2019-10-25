#模块

#引用内置库
import os    #引进os模块，详见a_test.py
import time
'''
time.sleep(2) #程序暂停2秒

time.time()#时间戳

datetime.time() #运行时间
'''
'''
import random
random.randint(0,10)  #伪随机

random.random()  #随机浮点数
'''
#引用第三方库
'''
安装外部库：pycharm -- preferences -- project interpreter -- + -- '选择库' -- install
相当于执行了：pip3 install requests

import requests

r = requests.get('https://www.baidu.com')
print(r.text)
'''

#建立自己的库：在库下建立一个__init__.py文件,或者系统自动生成
'''
from module import test1
test1.test()
'''
#文件读取
#r w a -->读 写（会覆盖文件中的内容） 追加写（末尾添加）读写文件性能会很低，因为文件存在磁盘，需要转到CPU运行
# w = open('open.txt','r')  #每次都只能操作一个方法
# w.write('测试写')
#
# w.close()          #文件操作后需要关闭，文件描述符

'''
r.readlines():一行一行读

'''
# r = open('open.txt','r')
# read_txt = ''
# while True:
#     x = r.read(1)
#     if len(x) == 0:
#         break
#     read_txt += x
# r.close()
# print(read_txt)

# r = open('open.txt','r')
# read_txt = ''
# while True:
#     x = r.readlines()
#     if len(x) == 0:
#         break
#     print(x)
# r.close()


# with open('open.txt','r') as r:  #在其中的文件操作代码运行后会自动关掉
#     read_txt = ''
#     while True:
#         x = r.readlines()
#         if len(x) == 0:
#             break
#         print(x)
