# -*- coding: utf-8 -*-
height = float(input("身長をm単位で入力して下さい>"))
weight = float(input("体重をkg単位で入力して下さい> "))
n = 2
bmi = (weight / height ** n)
print(bmi)
def him():
    if bmi < 18.5:
        print("あなたは肥満度はやせです")
    elif 18.5 <= bmi <25:
        print("あなたは肥満度は標準です")
    elif 25 <= bmi <30:
        print("あなたは肥満度は肥満です")
    else:
        print("あなたは肥満度は高度肥満です")
him()