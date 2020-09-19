# -*- coding: utf-8 -*-
'''
借金をして月々、定額を返済していくと借金はどうなっていくのかを調べるプログラムを作成しましょう。
借金の金額と、利息の年利率(%)、月々の返済額を入力すると、毎月、借金がなくなるまで月数と借金の金額を表示するものとする。
月々の借金は、借金の利息年利率/12（月割り）分増加するが、返済分だけ減る。
実行結果
借金> 100000
年利率(%)> 14.0
返済額> 20000
1月: 返済額 20000 円 残り 81166 円
2月: 返済額 20000 円 残り 62113 円
3月: 返済額 20000 円 残り 42838 円
4月: 返済額 20000 円 残り 23338 円
5月: 返済額 20000 円 残り 3610 円
6月: 返済額 3652 円 これで完済。 返済総額:  103652 円
'''

class Syakin:
    def __init__(self):
        self.syakin = None
        self.nenri = None
        self.hensai = None
        self.month = None
        self.total = None

    def syakinkeisan(self):
        self.syakin = input(int('借金>')
        self.nenri = input(float('年利率(%)>')
        self.hensai = input(int('返済額>')

        self.month = 0
        while self.syakin > self.hensai:
            self.month += 1
            self.syakin = self.syakin * (1 + nenri / 12 / 100) – hensai
            print(str(month) + “月：　返済額“, self.hensai, ”円 残り”, self.syakin, ”円“)

　　










