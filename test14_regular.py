'''
正则表达式：邮箱等规则字符串可用   re函数

模糊查询：判断主题是字符串
特殊字符：
\d:数字（一个数字（开始为数字则正确））
\D:非数字
\w:单词字符
\W:非单词字符
\s:空白字符
[1-9]: 1到9数字

转义符：\
\\d:\d
\.:.
.:任意字符

|：左右满足任何一个即可

正则表达式的数量：
*:0个或多个
+：1个或多个
？：0个或1个  贪婪模式下:取消贪婪模式
^:以xxx开头
$:以XXX结尾
\A:相当于：^\w
\Z:相当于:\w$
{0,5}：格式重复次数0到5次
r:转译符，r'  '

re函数
match:尽量不匹配，找到一个马上返回
search：
findall:尽量匹配

'''

import re


# pa = '\d'   #规则 --->正则表达式
# str1 = 'qaqsqdq12313'
#
# x = re.findall(pa,str1)
# print(x)

# def is_num(string1):
#     pattern = '\w+@\w+\.com'
#     x = re.findall(pattern,string1)
#     print(x)
#     return x
#
# while True:
#     str1 = input('输入邮箱： ')
#     res = is_num(str1)
#     if len(res) == 0:
#         print('xxxx')
#     else:
#         print('oooooo')
#         break

# def is_num(string1):
#     pattern = r"^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"
#     # pattern = r'1\d\d|25[0-5]|2[0-4]\d'
#     x = re.findall(pattern, string1)
#     print(x)
#     return x
#
#
# while True:
#     str1 = input('输入号码： ')
#     res = is_num(str1)
#     if len(res) != 1:
#         print('xxxx')
#     else:
#         print('oooooo')
#         break
# content = 'Hello 12345 World'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result.group())
#
# content = 'http://weibo.com/comment/kEraCNdsfgkdsfgjkldsjkl'
# result1 = re.match('http.*?comment/(.*?)', content)
# result2 = re.match('http.*?comment/(.*)', content)
# print('result1', result1.group(1))  # 结果 result1
# print('result2', result2.group(1))  # 结果 result2 kEraCN
#



# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result.group(1))  # 结果
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result.group(1))  # 结果 7

l = [1,2,3,[1,2,3]]
l1 = []