# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/25 下午7:14
# @File: test.py

a=[1,2,3,4,5]
# print(a)
b=a
# print(b.pop())

import os

def addFile(file1,file2):
    try:
        os.path.exists(file1)
        os.path.exists(file2)
        file1 = open(file1,'rb')
        file2 = open(file2,'rb')

        list1 = file1.readlines()

    # print(list1,type(list1))
        list2 = file2.readlines()

    # print(list2)

        list2.extend(list1)
    # print(list2)
    except Exception as e:
        print('not exit file')
    return list2

# new = addFile('1.txt','2.txt')
# print(new)


'''
file3 = open('3.txt','rb')
file4 = open('4.txt','rb')

list3 = file3.readlines()
list4 = file4.readlines()

list3_name = []
list3_phone = []
list4_name = []
list4_qq = []

for message in list3:
    temp_list = message.split()
    list3_name.append(str(temp_list[0].decode('utf-8')))
    list3_phone.append(str(temp_list[1].decode('utf-8')))
print(list3_name)
print(list3_phone)

for message in list4:
    temp_list = message.split()
    list4_name.append(str(temp_list[0].decode('utf-8')))
    list4_qq.append(str(temp_list[1].decode('utf-8')))
print(list4_name)
print(list4_qq)

list5 = []
for i in range(len(list3_name)):
    s = ''
    if list3_name[i] in list4_name:
        j = list4_name.index(list3_name[i])

    s = '\t'.join([[list3_name[i]],list3_phone[i],list4_qq[j]])
    s+='\n'
else:
    s = '\t'.join([[list3_name],list3_phone,str('------')])
    s+='\n'
list5.append(s)

print(list5)
'''

# class EchoDevice:
#     device = 'device'
#     def echo(self):
#         msg = 'This is a test'
#         m = msg+"from"+self.device
#         return m
'''
class Computer():
    screen = True
    def start(self):
        print('start')
a = Computer()
aa = a.screen
print(aa)
a.start()
'''

'''
class Echo():
    device = 'device001'
    def ech(self):
        str = 'this is a test from '
        print(str)
        return str

e = Echo()
string = e.ech()

device = e.device
print(device)

list = [string,device]
print(list)
newStr = ' '.join(list)
print(newStr)
'''




# print(f(3),f(256),f(100),f(3),f(255),f(-3))

import unittest
import numpy as np



class Test(unittest.TestCase):
    def commen(self,x):
        if x < 0:
            a = 2
            y= a*x
        elif x >= 0 & x <= 255:
            y=255 - x
        elif x > 255:
            a = 2
            y= a*x
        else:
            return None
        return y

    #测试<0
    def test_less0(self):
        x = -3
        a = 2
        y=self.commen(x)
        expect= x*a
        if y == expect:
            print('test_less0 test pass '+'expect='+str(expect)+' y='+str(y))

        else:
            print('test_less0 test fail')

    # 测试=0
    def test_equal0(self):
        x = 0
        y=self.commen(x)
        expect= 255-x
        if y == expect:
            print('test_equal0 test pass '+'expect='+str(expect)+' y='+str(y))
        else:
            print('test_equal0 test fail')

    # 测试等于255
    def test_equal255(self):
         x = 255
         y = self.commen(x)
         expect = 255-x
         if y == expect:
             print('test_equal255 test pass '+'expect='+str(expect)+' y='+str(y))
         else:
             print('test_equal255 test fail')

    # 测试大于255
    def test_moreThan255(self):
        x = 300
        a = 2
        y = self.commen(x)
        expect= x*a
        if y == expect:
            print('test_moreThan255 test pass '+'expect='+str(expect)+' y='+str(y))

        else:
            print('test_moreThan255 test fail '+'expect='+str(expect)+' y='+str(y))


if __name__ == '__main__':
    unittest.main()