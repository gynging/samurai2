# -*- coding: utf-8 -*
"""
数字を入力し、入力した数だけ画面に■印を表示するプログラムを書きなさい。
実行結果
数> 25
25:■■■■■■■■■■■■■■■■■■■■■■■■■
"""

kazu = int(input('数> '))

print(str(kazu)+':',end='')

for i in range(0,kazu):
    print('■',end='')





        