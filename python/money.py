# -*- coding: utf-8 -*-
"""
金額を入力するとその金額を出来るだけ少ない枚数の貨幣を使って支払えるように貨幣の枚数を数えるプログラムを書いてください。
貨幣は、{１万円札、五千円札、千円札、五百円玉、百円玉、五十円玉、十円玉、五円玉、一円玉}とする
余り使わないので２千円札は除く）。
実行結果
金額(円)> 48767
金額: 48767 円
一万円札= 4 枚
五千円札= 1 枚
千円札　= 3 枚
五百円玉= 1 枚
百円玉　= 2 枚
五十円玉= 1 枚
十円玉　= 1 枚
五円玉　= 1 枚
一円玉　= 2 枚
"""

money = int(input("金額(円)>"))
print("金額:" + str(money) + "円")
maisuu = money // 10000
money = money % 10000
print("一万円札= " + str(maisuu) + " 枚")
maisuu = money // 5000
money = money % 5000
print("五千円札= " + str(maisuu) + " 枚")
maisuu = money // 1000
money = money % 1000
print("千円札= " + str(maisuu) + " 枚")
maisuu = money // 500
money = money % 500
print("五百円玉= " + str(maisuu) + " 枚")
maisuu = money // 100
money = money % 100
print("百円玉= " + str(maisuu) + " 枚")
maisuu = money // 50
money = money % 50
print("五十円玉= " + str(maisuu) + " 枚")
maisuu = money // 10
money = money % 10
print("十円玉= " + str(maisuu) + " 枚")
maisuu = money // 5
money = money % 5
print("五円玉= " + str(maisuu) + " 枚")
maisuu = money // 1
money = money % 1
print("一円玉= " + str(maisuu) + " 枚")

"""
e = 45000
f = 10000
print(e // f) #4と出る
"""


