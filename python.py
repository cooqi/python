#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#print('10247*768=',10247*768);
#hello='hello';
#name=input('请输入你的姓名');
#print(hello,name)
#a=int(input('请输入一个数字'))#input 输入的是字符串，所以需要int成整数型
#if a >= 0: 
#    print(a)
#else:
#     print(-a)

#print('''hello 
#world
#中文''')

#s1=72
#s2=85
#r=((s2-s1)/s1)*100
#print('晓明成绩提升点为：%.1f%%' % r)


#l = [
#    ['Apple', 'Google', 'Microsoft'],
#    ['Java', 'Python', 'Ruby', 'PHP'],
#   ['Adam', 'Bart', 'Lisa']
#]
# 打印Apple:
#print(l[0][0])
# 打印Python:
#print(l[1][1])
# 打印Lisa:
#print(l[2][2])

#height = int(input('请输入您的身高：'))
#weight = int(input('请输入您的体重：'))
#bmi = weight/(height*height)
#if bmi<18.5:
#    print('您的bmi为：%.2f ，体重过轻' % bmi)
#elif bmi<25 and bmi>18.5:
#    print('您的bmi为：%.2f ，体重正常' % bmi)
#elif bmi<28 and bmi>25:
#    print('您的bmi为：%.2f ，体重过重' % bmi)
#elif bmi<28 and bmi>32:
#    print('您的bmi为：%.2f ，体重肥胖' % bmi')
#elif bmi>32:
#    print('您的bmi为：%.2f ，体重严重' % bmi)

#sum=0
#nums=[1,2,3,4,5,6,7,8,9,10,11]
#for num in nums:
#    sum=sum+num
#print(sum)

#s=0
#n=99
#while n>0:
#    s = s+n
#    n = n-1
#print(s)

#l=['cooqi','list','adam']
#for ls in l:
#   print('hello,',ls,'!')

#names=['cooqi','list','adam']
#x=0
#y=len(names)
#while x<y:
#    print('hello,',names[x],'!')
#    x=x+1

#def my_abs(x):
#    if x >= 0:
#        return x
#   else:
#       return -x

import math
def quadratic(a, b, c):
    z=b*b - 4*a*c
    if z>=0:
	    x1=-b + math.sqrt(z)/2*a
	    x2=-b - math.sqrt(z)/2*a
	    return x1,x2
    else:
	    print('无解')
print(quadratic(2,3,1))