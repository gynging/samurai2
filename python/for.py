# -*- coding: utf-8 -*-
'''
この処理はFORです。
'''
for i in range(1, 31, 1):
    '''
    この処理はFORです。
    '''
    if i % 3 == 0:
        print("三の倍数です！")
    elif i % 5 == 0:
        continue
    else:
        print (i)
    print("森本眞一郎")
else:
    print("for文終わりました！")