# -*- coding: utf-8 -*-
"""
健康のために肥満度をチェックしてみましょう。身長と体重を入力してあなたの肥満度（BMI＝体重(kg)÷身長(m)の二乗）を計算するプログラムを作成し、計算結果を確かめてください。
確かめた結果も出力して下さい
　判定基準が18.5未満→やせ、18.5〜25未満→標準、25〜30未満→肥満、30以上→高度肥満となっているようです。
実行結果
身長をm単位で入力して下さい> 1.70
体重をkg単位で入力して下さい> 65
BMI = 22.49134948096886
あなたは肥満度は標準です。
"""
class Bmi:
    def __init__(self):
        self.height = None
        self.weight = None
        self.karadaflag = None

    def say_karada(self):
        while self.karadaflag == None:
            try:
                self.height = float(input("身長をm単位で入力して下さい>" ))
                self.weight = float(input("体重をkg単位で入力して下さい>" ))
                self.karadaflag = 1
            except SyntaxError:
                print("数値で入力してください")
            except NameError:
                print("数値で入力してください")

    def bmi(self):
        self.n = 2
        self.bmi = (self.weight / self.height ** self.n)

    def him(self):
        if self.bmi < 18.5:
            print("あなたは肥満度はやせです")
        elif 18.5 <= self.bmi < 25:
            print("あなたは肥満度は標準です")
        elif 25 <= self.bmi < 30:
            print("あなたは肥満度は肥満です")
        else:
            print("あなたは肥満度は高度肥満です")

bbmi = Bmi()

bbmi.say_karada()

bbmi.bmi()

bbmi.him()





