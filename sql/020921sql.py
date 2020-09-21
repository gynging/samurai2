# coding=utf-8
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()
#c.execute("create table mydrinkcount(drinkkind,buycount)")
c.execute("INSERT INTO mydrinkcount VALUES ('コーラ','1')")
c.execute("select * from mydrinkcount where buycount = '1'")
d = c.fetchone()
print(d)
e = d[1]
print(e)
c.execute("update mydrinkcount set buyconut=? where drinkkind=?",(e,d[1]))
c.execute("select * from mydrinkcount where drinkkind = 'コーラ'")
print(c.fetchone())
dbfile2.commit()
dbfile2.close()
"""
dbfile = sqlite3.connect('zannsuu.db')
c = dbfile.cursor()
#c.execute("create table vendingcount(vendingdrinkkind,count)")
c.execute("INSERT INTO vendingcount VALUES ('コーラ',1)")
c.execute("select * from vendingcount where vendingdrinkkind = 'コーラ'")
print(c.fetchone())
dbfile.commit()
dbfile.close()
"""
