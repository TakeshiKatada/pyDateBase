import sqlite3

#COSMOS.dbに接続
conn=sqlite3.connect("Sample.db", isolation_level=None)

#データ取得
c=conn.cursor()
c.execute("SELECT * FROM Fruit")
for row in c:
    print(row[0],row[1],row[2])

conn.close()