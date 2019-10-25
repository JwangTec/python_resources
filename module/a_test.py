#内置模块

'''

os模块
path函数os模块中的abspath:找出当前运行函数的绝对路径
os.mkdir:不能递归创建目录
os.path.join:相当于"+/"，如果是windos则是"\+"
os.makedirs: 可递归创建文件
os.path.abspath:显示文件的绝对路径
os.path.dirname:显示文件上层目录
os.rmdir:删除空文件
shutil模块
shutil rmtree:强制删除文件
shutil move:移动文件
shutil copy:
shutil copytree:
'''
import os
import shutil #更高级一点的库

# def get_path():
#     xx =os.path.abspath(__file__)
#     return xx
#
#
#


#一直找上层路径直到项目路径
# c_path = os.path.abspath(__file__)
# module_path = os.path.dirname(c_path)
# pycode_path = os.path.dirname(module_path)

#
# print(os.path.dirname(pycode_path))

#相当于下面代码
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# print(BASE_DIR)
# os.mkdir(BASE_DIR+'/b_test')


# xx = os.path.join(BASE_DIR,'text1','text2') #在BASE_DIR的路径下创建text1并在该文件下再创建text2
# os.mkdir(xx)   #不能递归创建
# os.makedirs(xx) #可递归创建文件
# os.makedirs(xx,exist_ok=True)  #若有该文件名存在则不会再报错

# os.rmdir(os.path.join(BASE_DIR,'b_test'))  #只能删除空目录

#shutil.rmtree(os.path.join(BASE_DIR,'text1')) #使用shutil库函数删除文件夹

# os.mkdir(os.path.join(BASE_DIR,'a_text'))
# os.mkdir(os.path.join(BASE_DIR,'b_text'))
# shutil.move(os.path.join(BASE_DIR,'a_text'),os.path.join(BASE_DIR,'b_text'))  #将位于BASE_PATH路径下的a_text移动到b_text下



# shutil.copy('test1.py','test4.py')   #拷贝文件到一个新文件中  操作的是文件
# shutil.copytree(os.path.join(BASE_DIR,'module'),os.path.join(BASE_DIR,'module2')) # 拷贝文件夹到新文件夹中，操作的是文件夹

# yy = os.listdir(BASE_DIR+'/module')  #遍历文件夹
# print(yy)

