import module.test1    #引用目标文件名     会先执行import下的文件
import module.a_test
print(module.test1.a_test())  #直接调用该文件下的为a_test的函数，并打印输出  若有其它文件调用该文件下函数，会执行该文件下的命令，解决方案见a_test.py
print(module.test1.test())    #会先执行module下test1中的所有，再执行函数test若无return会返回空
print(module.a_test.get_path())  #调用的执行目标文件所在路径，而不是这一个文件的路径