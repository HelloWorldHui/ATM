# coding=utf
"""
author=Hui_T
"""

def f():
    data_list = []
    with open('user_info.txt','r',encoding='utf8') as f :
        for line in f:
            data_list.append(line)
    return data_list

data = f()
print(data)
for i in data:
    print(i)
l = ['1','2','3']
s = ','.join(l)+'\n'
print(s)

print(12300%100 == 0)
print(set('11111'))

class A:
    def __init__(self,num):
        if num == 0:
            return
    def a(self):
        print(1)
a = A(0)
a.a()