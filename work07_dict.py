
'''
备注：字典部分案例较多，根据情况自由选择，也可以作为综合练习和复习使用；后期class课程结束后，也可以选择本节课案例完成

案例1：实现如下效果、详见课件中的图片.jpg案例

#案例2：
# 根据以下场景，模拟一个自助购物系统：
# 场景：市场上有一家新店开业，为了吸引顾客光临，现将部分商品出售，派克钢笔（单价200）、茶杯(单价50)、毛巾(单价20)、书(单价20)、拖鞋(单价10)等商品，每位顾客进店，可手持一个购物车进行选购商品，选购完成后，总价在500元以上时，商家会优惠50元，1000元优惠100元，依次累加优惠政策，结账时可直接抵现；
# 功能细则如下：
# 1）可查看目前商品信息（商品名及单价）；
# 2）查看当前购物车中商品信息：需要显示当前商品名称、商品单价、当前购物车商品数量等相关信息，以及购物车中商品总价；
# 3）添加商品到购物车：可根据商品名称，放入购物车中（默认添加一件）；
# 4）减少移出购物车中的指定商品；
# 5）结账，离开购物车系统，显示最终价格及购买的商品列表明细；

def List_of_Commodities():                  #商城存在的商品
    list_commodities = {'pencil':200,'cup':50,'towei':20,'book':20,'slipper':10}
    return list_commodities
def shopping_cart():                      #购物车商品清单（需要先进行添加删除）
    shopping_list = del_shopping_cart()
    list_commo = List_of_Commodities()
    sum_shopping = 0
    print("当前购物车商品清单：")
    for i in shopping_list.keys():
        if i in list_commo.keys():
            prace = shopping_list[i] * list_commo[i]
            sum_shopping += prace
            print("商品名称：%s\t 商品单价：%d \t商品数量：%d \t该商品总价：%d"%(i,shopping_list[i],list_commo[i],prace))
    return sum_shopping

def add_shopping_cart():              #添加商品到购物车 每次选择商品都为1单位增加
    shopping_list1 = {}
    star_shopping = 1
    while star_shopping:
        add_shopping = input('请输入需要添加的商品名：')
        if add_shopping in List_of_Commodities():
            if add_shopping in shopping_list1.keys():
                shopping_list1[add_shopping] += 1
            else:
                shopping_list1[add_shopping] = 1
        else:
            print('请重新在以下商品中选择：')
            for i in List_of_Commodities().keys():
                print(i)
        xx = input("停止添加请按0：")
        if xx == '0':
            star_shopping = int(xx)
        else:
            star_shopping = 1

    return shopping_list1

def del_shopping_cart():   #删除购物车中存在的商品,每次删除数量都以1为单位
    shopping_list2 = add_shopping_cart()
    del_cart = input("是否需要删除商品 yes/no： ")
    while del_cart == 'no':
        break
    is_del = True
    while is_del:
        del_name = input('请输入需要删除的商品名：')
        if del_name in shopping_list2:
            if shopping_list2[del_name] == 1:
                del shopping_list2[del_name]
            else:
                shopping_list2[del_name] -= 1
        else:
            print('请重新在以下商品中选择：')
            for i in shopping_list2.keys():
                print(i)
        xx = input("是否继续删除 yes/no : ")
        if xx == 'yes':
            is_del = True
        else:
            is_del = False
    return shopping_list2


def end_sum_cart():              #计算总价，整个功能实现只需要运行该函数即可
    discount = 0
    sum_shopping = shopping_cart()
    xx = sum_shopping // 500
    for i in range(xx):
        discount += 50
    end_shopping_prace = sum_shopping - discount
    print('商品优惠%d,当前购物车中商品总价为%d'%(discount,end_shopping_prace))

end_sum_cart()
'''


#扩展：
# 思考：无答案
# 面食，面食下面有方便面和鸡蛋面
# 水果，水果下面有苹果、桃子、葡萄、香蕉、西瓜
# 水产品，水产品下面有鲫鱼、草鱼
# 酒水，酒水下面有红酒、白酒、啤酒
#
# 根据上述，整理一个数据结构，并对数据可以进行添加（数量）、jian少（数量）
# 查询（所有商品以及添加过的商品）
'''
def detailed_list():   #所有商品名清单
    detailed_list = {'面食':['方便面',"鸡蛋"],'水果':['苹果','桃子','葡萄','香蕉','西瓜'],'水产品':['鲫鱼','草鱼'],'酒水':['红酒','白酒','啤酒']}
    return detailed_list
print(detailed_list()['面食'][:])

def add_detailed_list():             #添加名称以及数量
    add_list = {}
    is_add = True
    while is_add:
        add_name = input('请输入需要添加的名称：')
        num_name = int(input('请输入%s的添加数量：'%add_name))

        detailed_list1 = detailed_list()
        for name_list in detailed_list1:
            name_list_value = detailed_list1[name_list]
            for name in name_list_value:
                if add_name == name:
                    if add_name in add_list.keys():
                        add_list[add_name] += num_name
                    else:
                        add_list[add_name] = num_name
                        xx = input("继续添加请按yse: ")
        if xx == 'yes':
            is_add  = True
        else:
            is_add  = False
    return add_list

def del_detailed_list():             #删除数量及名称
    list_detailed = add_detailed_list()
    print('添加的商品以及数量如下：')
    print(list_detailed)
    del_is = input('是否需要删除yes/no: ')
    while del_is == 'no':
        break
    del_loop = True
    while del_loop:
        name_del = input('请输入需要删除的名称： ')
        if name_del in list_detailed.keys():
            num_del = int(input('删除%s的数量为： ' % name_del))
            if num_del > list_detailed[name_del]:
                print('删除数量超过总数量%d请重新输入'%list_detailed[name_del])
                num_del = int(input('删除%s的数量为： ' % name_del))
            elif num_del == list_detailed[name_del]:
                del list_detailed[name_del]
            else:
                list_detailed[name_del] -= num_del
        aa = input('是否继续删除yes/no: ')
        if aa == 'yes':
            del_loop = True
        else:
            del_loop = False
    return list_detailed

def information_list():    #查询清单
    print('添加过的商品有：')
    print(add_detailed_list().keys())
    print('现在存在的所有商品有：')
    for i in del_detailed_list().items():
        print(i)

'''


#案例3：
# 学校有五个社团，现在对五个社团进行招生，将学生的姓名进行报备
# 1、一个学生可以报多个社团，不能重复报同一个社团（不考虑同名的情况）
# 2、可以取消在某个社团的报名
# 3、可以查看某个学生所报的所有社团名字
# 4、可以查看某个社团下的所有名字
# 提示：
# 已知一个数据结构
# students = {'chinese': [], 'math': [], 'english': [], 'music': [], 'artist': []}
# 注意用户体验

'''
students = {'chinese': [], 'math': [], 'english': [], 'music': [], 'artist': []}
def showmenu():
    print('1:显示所有社团名称:')
    print('2:选择社团报名:')
    print('3:查询该学生报名社团情况:')
    print('4:取消报名,选择社团名称:')
    print('5:查看某个社团的学生名字:')
    n = int(input('请选择:'))
    return n

def name_num():
    print('当前学生社团名称如下:chinese math english music artist ')

def apply(student):

    print('当前学生社团名称如下:chinese math english music artist ')
    group = input('输入要报名的社团：')
    if group not in list(student.keys()):
        print('您输入的社团不存在！')
    else:
        name = input('输入学生姓名：')
    if name in student[group]:
        print('你已经报名过该社团，不能重复报名！')
    else:
        student[group].append(name)
        print('报名成功！')

def delapply(student):
    print('当前学生社团名称如下:chinese math english music artist ')
    group = input('输入要取消报名的社团：')
    if group not in list(student.keys()):
        print('您输入的社团不存在！')
    else:
        name = input('输入需要移除的学生姓名：')
    if name not in student[group]:
        print('你输入姓名的学生在当前科目没有报名！')
    else:
        student[union].remove(name)
        print('取消报名成功！')

def mypersonal(student):
    name = input('输入查看的学生姓名：')
    s = ''
    for group,nam in student.items():
        for name1 in student[group]:
            if name1 == name:
                s += '+group'
    print('学生{},报名的社团有{}'.format(name,s))

def showstudents(student):
    print('当前学生社团名称如下:chinese math english music artist ')
    group = input('输入查看该社团：')
    if group not in list(student.keys()):
        print('您输入的科目不存在！')
    else:
        print('社团报名信息如下：')
    print(list(map(lambda stu:print(stu),student[group])))


while True:
    n = showmenu()
    if n == 2:
        apply(students)
    elif n == 3:
        delapply(students)
    elif n == 4:
        mypersonal(students)
    elif n == 5:
        showstudents(students)
    elif n == 1:
        name_num()
    else:
        break

'''
