import sqlite3, csv

conn = sqlite3.connect('toolroom.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tools(
id TEXT   PRIMARY KEY   NOT NULL ,
desc    TEXT ,
remarks    TEXT ,
location TEXT ,
issue TEXT
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS users(
id TEXT   PRIMARY KEY   NOT NULL
);''')



