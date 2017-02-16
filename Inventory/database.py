import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(
nsn INT PRIMARY KEY      NOT NULL,
pn    TEXT NOT NULL,
desc    TEXT NOT NULL,
remarks    TEXT NOT NULL,
location TEXT NOT NULL,
niin TEXT NOT NULL
);''')