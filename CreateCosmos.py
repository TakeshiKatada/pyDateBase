#Cosmos.dbを作成して、Menberテーブルを作成し、四人分登録するプログラム

import sqlite3

conn = sqlite3.connect("Cosmos.db", isolation_level=None)

sql="""
create table Menber (
    id vaechar(4),
    name varchar(20),
    age integer,
    email varchar(128)
);
"""

conn.execute(sql)

conn.execute("INSERT INTO Menber VALUES ('1018','Kenta',23,'ken@py.co.jp')")
conn.execute("INSERT INTO Menber VALUES ('1027','Yamano',18,'yamachan@ab.cd')")
conn.execute("INSERT INTO Menber VALUES ('1135','Honda',28,'honda@car.co.ja')")
conn.execute("INSERT INTO Menber VALUES ('1333','Tomita',32,'tommy@@py.co.ja')")

c = conn.cursor()
c.execute("SELECT * FROM Menber")
for row in c:
    print(row[0],row[1],row[2],row[3],)

conn.close()
