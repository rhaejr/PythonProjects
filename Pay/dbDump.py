import sqlite3, json

conn = sqlite3.connect('wages.db')
cur = conn.cursor()

cur.execute('select * from counties')
