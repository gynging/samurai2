# coding=utf-8
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()
#c.execute("create table mydrinkcount(drinkkind,buycount)")
c.execute("INSERT INTO mydrinkcount VALUES ('コーラ','1')")
c.execute("select * from mydrinkcount where buycount = '1'")
d = c.fetchone()
print(d)

"""
e = 2
print(e)
c.execute("update mydrinkcount set buycount=? where drinkkind=?",(e,d[0]))
c.execute("select * from mydrinkcount where drinkkind = 'コーラ'")
print(c.fetchone())
dbfile2.commit()
dbfile2.close()
"""

c.execute("create table zihannkicount(drinkkind,buycount)")
c.execute("INSERT INTO  zihannkicount VALUES ('コーラ','10')")
c.execute("INSERT INTO zihannkicount VALUES ('ソーダ','10')")
c.execute("INSERT INTO zihannkicount VALUES ('オレンジジュース','10')")
dbfile2.commit()
dbfile2.close()

