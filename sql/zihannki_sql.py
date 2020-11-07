# -*- coding: utf-8 -*-
import os
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()
"""
メニュー画面を作成
　メニュー内容
　　・自動販売機飲み物購入機能
　　　→ 今まで課題で作成した自動販売機プログラム搭載
　　・販売機編集
　　　→ 以下機能を含んでいる
　　　　　1 自動販売機飲み物個数追加機能
　　　　　　→ 既存の飲み物の個数をユーザーが指定した個数に追加できる
　　　　　2 自動販売機飲み物種類追加機能
　　　　　　→ 既存の飲み物に加えて新しい種類の飲み物を買えるようにする
　　　　　3 自動販売機飲み物種類削除機能
　　　　　　→ 既存の飲み物をユーザーが任意に削除できるようにする
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
        self.menukind = None
        self.menukist = None
        self.choice = None
        self.choicekind = None
        self.choicemenu = None
        self.add = None
        self.kind = None
        self.newkind = None
        self.deletedrink = None
        self.editlist = None
        self.editlist2 = None
        self.control1 = None
        self.control2 = None

    def menu(self):
        self.menukind = ["1:自動販売機飲み物購入機能","2:販売機編集"]
        for self.menulist in self.menukind:
            print(self.menulist)

        while self.control1 == None:
            self.choicemenu = int(input("どちらかを数字で選んで下さい"))
            if self.choicemenu == 1:
                zihann.say_nomitaimono()
                zihann.tudukemasuka()
                self.control1 == 1


            elif self.choicemenu == 2:
                self.control1 == 1
                self.editlist = ["1 自動販売機飲み物個数追加機能","2 自動販売機飲み物種類追加機能","3 自動販売機飲み物種類削除機能"]
                for self.editlist2 in self.editlist:
                    print(self.editlist2)
                    while self.control2 == None:
                        self.editcommnd = int(input("1か2か3で選んで下さい"))
                        if self.editcommnd == 1:
                            self.control2 = 1
                            zihann.addrink()


                        elif self.editcommnd == 2:
                            zihann.addkind()
                            self.control2 = 1

                        elif self.editcommnd == 3:
                            zihann.editdrink()
                            self.control2 = 1
                        else:
                            continue
            else:
                print("1か2で選んで下さい。")



    def addrink(self):
        self.add = str(input("どの飲み物を追加しますか？"))
        c.execute("select * from zihannkicount where drinkkind = ? ", (self.add,))
        m = c.fetchone()
        n = int(m[1]) + 1
        c.execute("update zihannkicount set buycount=? where drinkkind=?", (n, self.add))

    def addkind(self):
        self.newkind = str(input("なんという飲み物を追加しますか？"))
        c.execute("insert into zihannkicount values ('self.newkind','10')")
        c.execute("select * from zihannkicount")
        d = c.fetchall()
        print(d)

    def editdrink(self):
        self.deletedrink = str(input("なんという飲み物を消去しますか？"))
        c.execute("delete from zihannkicount where drinkkind = ?",(self.deletedrink))
        c.execute("select * from zihannkicount")
        d = c.fetchall()
        print(d)

    def say_zyusu(self):
        print("コーラは100円です。ソーダは150円です。オレンジジュースは300円です。")

    def say_nomitaimono(self):
        print("コーラは100円です。ソーダは150円です。オレンジジュースは300円です。")
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
                        c.execute("select * from mydrinkcount where drinkkind = ?",(self.kin,))
                        i = c.fetchone()
                        print("{0}の購入数はこれで{1}個目です".format(self.kin,i[1]))
                    else:
                        self.sagaku = self.zyusu[self.kin] - self.kig
                        print("お金が{}円足りません。".format(self.sagaku))
                except SystemError:
                    print("数値で入力してください")
            else:
                print("在庫がありません")
        else:
            print("売り切れです")

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

    zihann.menu()

    zihann.tudukemasuka()

dbfile2.commit()
dbfile2.close()








