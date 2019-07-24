#Customer.dbを作成して、Fruitテーブルを作成し、四人分登録するプログラム

import sqlite3

conn = sqlite3.connect("Sample.db", isolation_level=None)

sql="""
create table Customer (
    id vaechar(4),
    name varchar(20),
    address varchar(128)
);
"""

conn.execute(sql)

sql="""
create table Fruit (
    id vaechar(4),
    name varchar(20),
    price integer
);
"""

conn.execute(sql)

conn.execute("INSERT INTO Fruit VALUES ('2222','lemon',100)")
conn.execute("INSERT INTO Fruit VALUES ('3333','apple',200)")
conn.execute("INSERT INTO Fruit VALUES ('4444','nasi',300)")
conn.execute("INSERT INTO Fruit VALUES ('5555','painapple',400)")

conn.close()
