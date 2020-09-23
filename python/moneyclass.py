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

class Money:
    def __init__(self):
        self.money = None
        self.maisuu = None

    def calc(self):
        self.money = int(input("金額(円)>"))

        print("金額:" + str(self.money) + "円")

        self.maisuu= self.money // 10000
        self.money= self.money % 10000
        print("一万円札= " + str(self.maisuu) + " 枚")

        self.maisuu= self.money // 5000
        self.money = self.money % 5000
        print("五千円札= " + str(self.maisuu) + " 枚")

        self.maisuu = self.money // 1000
        self.money = self.money % 1000
        print("千円札= " + str(self.maisuu) + " 枚")

        self.maisuu = self.money // 500
        self.money = self.money % 500
        print("五百円玉= " + str(self.maisuu) + " 枚")

        self.maisuu = self.money // 100
        self.money = self.money % 100
        print("百円玉= " + str(self.maisuu) + " 枚")

        self.maisuu= self.money // 50
        self.money = self.money % 50
        print("五十円玉= " + str(self.maisuu) + " 枚")

        self.maisuu = self.money // 10
        self.money = self.money % 10
        print("十円玉= " + str(self.maisuu) + " 枚")

        self.maisuu = self.money // 5
        self.money = self.money % 5
        print("五円玉= " + str(self.maisuu) + " 枚")

        self.maisuu = self.money // 1
        self.money= self.money % 1
        print("一円玉= " + str(self.maisuu) + " 枚")

moneycalc = Money()

moneycalc.calc()

