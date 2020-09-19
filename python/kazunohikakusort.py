# -*- coding: utf-8 -*-
"""
３つの数を入力し、数を昇順に並べ替えてから出力するプログラムを作成してください。
実行結果
数1> 55
数2> 25
数3> 13
13 25 55
"""
a = int(input('数1> '))
b = int(input('数2> '))
c = int(input('数3> '))

numlist = [a,b,c]

numlist.sort()
for num in numlist:
    print(num,end=" ")