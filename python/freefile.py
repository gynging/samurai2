# -*- coding: utf-8 -*-
shakkin = int(input('借金> '))
riritsu = float(input('年利率(%)> '))
hensai =  int(input('返済額> '))
total = 0
month = 0
while shakkin > hensai :
    month += 1
    shakkin = shakkin*(1 + riritsu/12/100) - hensai
    print(str(month)+'月: 返済額',hensai,'円','残り',\
    int(shakkin),sep=' ')
    total += hensai
month += 1
shakkin = shakkin*(1 + riritsu/12/100)
total += shakkin
print(str(month)+'月: 返済額',int(shakkin),'円','これで完済。','返済総額: ',\
int(total),'円',sep=' ')

