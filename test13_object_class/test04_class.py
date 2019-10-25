'''
异常类 ：报告错误 --> 中断 运行

'''
#只会监听特殊类型的错误
try:
    xx = [qxaas]
except NameError:      #监听与 NameError 相关的错误，监听所有报错只需要监听其父类（Exception）即可
    print('cuo  wu')

# class TestError(Exception):  #exception属于报错的父类，继承即可


class TestError(Exception):  #自定义一个报错
    pass
def rujiao(age):
    if age < 30:
        print(age)
    else:
        raise TestError('xiajibaluanxie')  #报错目标 ：中止程序，并输出错误提示
# try:                #出现报错并继续运行后面的代码
#     rujiao(333)
# except TestError:
#     print("xxx")   #若输入pass 则会直接跳过并不会报错
#
# print('xxxxxxxxxx')
l = [1,2,3,4]
try:                #出现报错并继续运行后面的代码
    l[7]             #出现错误则直接报错，不会执行下面的语句快
    rujiao(60)
except TestError as errortype:  #打印错误提示 (as后接错误提示)   可以重复抓取不同的错误，显示抓取的只有一种
    print(errortype)
except IndexError:
    print("下标错误")
except AttributeError:
    print('无法赋值')
else:  #上述若未发现错误，就执行else中语句
    print('++++++++')
finally:  #若上述未出现错误或中断：至少会执行该命令
    print('-------')

print('xxxxxxxxxx')
