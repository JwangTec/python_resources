class User():
    def __init__(self,telephone,name,category,salary = 0):
        self.id = telephone
        self.name = name
        self.start_salary = salary
        self.category = category

class Staff(User):
    user_name = {}
    user_salary = {}
    user_category = {}
    def __init__(self,telephone,name,category,salary):
        super().__init__(telephone,name,category,salary)
        Staff.user_name[self.id] = self.name
        Staff.user_salary[self.id] = self.start_salary
        Staff.user_category[self.id] = self.category

    def makingcard(self,teleph,category):
        if category == 1 and teleph in Staff.user_category:
            print("你拥有卡片")
        else:
            self.category = category
            self.id = teleph
            Staff.user_category[teleph] = category

s1 = Staff(111,'aa',1,1000)
print(s1.user_category)

s1.makingcard(111,1)
s1.makingcard(1,1)
print(s1.user_category)






# def showmenu():
#     print('1:选择制作卡类:')
#     print('2:显示用户卡片详细信息:')
#     print('3:查询该用户拥有卡情况:')
#     print('4:注销卡片，选择注销卡片类别:')
#     print('5:1类卡充值:')
#     print('6:查看所有卡片状态：')
#     n = int(input('请选择:'))
# return n