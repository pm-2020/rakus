import sqlite3
con = sqlite3.connect('chat.db')
cur = con.cursor()
cur.execute("drop table if exists chat")
cur.execute('''create table chat (name text, sentence text)''')
con.commit()
con.close()