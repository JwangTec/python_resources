import os
import shutil

def deep_first(dir):  #深度遍历文件夹
    dir_lists = os.listdir(dir)
    if len(dir_lists) == 0:
        return
    for d in dir_lists:
        print(d)
        deep_first(os.path.join(dir,d))
deep_first('test')

def brand_first(dir):   #广度遍历文件夹
    buckets = []
    buckets.append(dir)

    while len(buckets) > 0:
        tmp = buckets.pop(0)
        print(tmp)
        files = os.listdir(tmp)    #listdir中容易乱序，需要排序
        files.sort()
        for i in files:
            buckets.append(os.path.join(tmp,i))

brand_first('test')

l = [1,2,3,[1,2,3]]
l1 = l[:]
l.append(5)
l[3].append(8)
print(l)
print(l1)
