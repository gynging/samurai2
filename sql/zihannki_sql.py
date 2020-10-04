# -*- coding: utf-8 -*-
import os
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()
"""
以前作成した自動販売機プログラムにてSQLを使用して、
改良してください。
用意するデータベースは二つ
一つは自販機の飲み物の残数などを設定するデータベース
もう一つは自分で購入した飲み物を管理するデータベース
飲み物に数量を設定し、
毎回買うごとに自動販売機のストック数から-1し、
自分で購入した履歴を持つデータベースには購入数 +1を行う。
自動販売機のストック数がない場合は
「売り切れです」
のようにメッセージを出力するようにする。
購入できた場合、
「XXXの購入数これでX個目です」
のように出力する。
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
            c.execute("select * from zihannkicount where drinkkind = ? ",(self.kin,))
            d = c.fetchone()
            a = d[1]
            if a != 0:
                self.kig = int(input("お金を投入してください"))
                try:
                    if self.zyusu[self.kin] <= self.kig:
                        self.oturi = self.kig - self.zyusu[self.kin]
                        if self.oturi == 0:
                            print("お釣りは有りません")
                        else:
                            print("お釣りは{}".format(self.oturi))
                        f = int(d[1]) - 1
                        c.execute("update zihannkicount set buycount=? where drinkkind=?", (f, self.kin))
                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                        g = c.fetchone()
                        h = int(g[1]) + 1
                        c.execute("update mydrinkcount set buycount=? where drinkkind=?", (h, self.kin))
                    else:
                        self.sagaku = self.zyusu[self.kin] - self.kig
                        print("お金が{}円足りません。".format(self.sagaku))
                except SystemError:
                    print("数値で入力してください")
            else:
                print("在庫がありません")
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

dbfile2.commit()
dbfile2.close()







