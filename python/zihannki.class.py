# -*- coding: utf-8 -*-
import os
"""
自動販売機プログラムを作成して下さい。
最初にコンソールに購入できる飲み物を出力させて下さい。
その後
キーボードから入力を行わせ、
入力された文言に対して判定をかけて
該当商品が存在すれば投入金額を入力させ、
該当商品ががない場合は、
「該当商品がありません」とメッセージを出力させ、
購入を続けるか問いて下さい。
投入金額を入力後
足りない場合は
「投入金額が不足しています」
「○○○○○円足りません」
と出力させる。
足りた場合且つ、お釣りが出る場合、
「○○○○を購入しました。」
「お釣りは￥○○○です」
と出力させる
購入を続けるか、購入を終了するかを選ばせ
続ける場合は、画面をクリアして
自動販売機の商品を再度表示させ
終了する場合はそのままプログラムを終了させる
"""

class Zihan:
    def __init__(self):
        self.kin = None
        self.zyusu = None
        self.kig = None
        self.oturi = None
        self.sagaku = None
        self.yesno = None
        self.modoru = None
        self.owariflag = None


    def say_zyusu(self):
        print("コーラは100円です。ソーダは150円です。オレンジジュースは300円です。")

    def say_nomitaimono(self):
        self.kin = str(input("飲みたいものを入力してください"))
        self.zyusu = {"コーラ":100,"ソーダ":150,"オレンジジュース":300}

        if self.kin in self.zyusu:

            self.kig = int(input("お金を投入してください"))
            try:
                if self.zyusu[self.kin] <= self.kig:
                    self.oturi = self.kig - self.zyusu[self.kin]
                    if self.oturi == 0:
                        print("お釣りは有りません")
                    else:
                        print("お釣りは{}".format(self.oturi))
                else:
                    self.sagaku = self.zyusu[self.kin] - self.kig
                    print("お金が{}円足りません。".format(self.sagaku))
            except SystemError:
                print("数値で入力してください")

        else:
            print("該当商品が有りません。")

    def tudukemasuka(self):
        self.modoru = None
        while self.modoru == None:

            self.yesno = input("購入を続けますか？yesかnoで入力して下さい。")

            if self.yesno == "yes":
                os.system('clear')
                self.modoru = 1

            elif self.yesno == "no":
                print("お疲れ様でした")
                self.owariflag = 1
                self.modoru = 1

            else:
                print("yesかnoで入力して下さい")


zihann = Zihan()


while zihann.owariflag == None:

    zihann.say_zyusu()

    zihann.say_nomitaimono()

    zihann.tudukemasuka()




























