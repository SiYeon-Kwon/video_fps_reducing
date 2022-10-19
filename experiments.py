import os

path = r'/home/kwon/compression/image_undouble'

file_list = os.listdir(path)

file_list.sort()
dic = {0:'0'}
for i in range(len(file_list)):
    try:
        value=file_list[i].split('_')
        key_value=value[0]
        max_num=0
        num=value[1].replace('.jpg','')
        num=int(num)
        if max_num<num:
            max_num=num
        dic[key_value]=max_num
    except:
        continue
print(value[0],dic)

