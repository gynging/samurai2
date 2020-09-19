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
zih = None


while zih == None:
    print("コーラは100円です。ソーダは150円です。オレンジジュースは300円です。")

    kin = str(input("飲みたいものを入力してください"))

    zyusu = {"コーラ":100,"ソーダ":150,"オレンジジュース":300}

    if kin in zyusu:
        kig = int(input("お金を投入してください"))
        try:
            if zyusu[kin] <= kig:
                oturi = kig - zyusu[kin]
                if oturi == 0:
                    print("お釣りは有りません")
                else:
                    print("お釣りは{}".format(oturi))
            else:
                sagaku = zyusu[kin] - kig
                print("お金が{}円足りません。".format(sagaku))
        except SystemError:
             print("数値で入力してください")

    else:
        print("該当商品が有りません。")

    zih2 = None

    while zih2 == None:

        yesno = input("購入を続けますか？yesかnoで入力して下さい。")

        if yesno == "yes":
            os.system('clear')
            zih2 = 1

        elif yesno == "no":
            print("お疲れ様でした")
            zih = 1
            zih2 = 1

        else:
            print("yesかnoで入力して下さい")
























