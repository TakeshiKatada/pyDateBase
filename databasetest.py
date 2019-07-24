# 必要モジュールをインポートする
import sqlite3

# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE employee(id, name, email, birtyday, section_id, memo)''')

# データの挿入
c.execute("INSERT INTO employee VALUES (1, '平林 太郎','hira@hi-ad.jp', '2001-01-01', 1, 'えらい')")
c.execute("INSERT INTO employee VALUES (2, '平林 次郎','hira@hi-ad.jp', '2005-01-01', 2, '明るい')")
c.execute("INSERT INTO employee VALUES (3, '平林 三郎','hira@hi-ad.jp', '2008-01-01', 3, 'すごい')")

# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()