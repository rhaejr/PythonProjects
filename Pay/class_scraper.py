import sqlite3

conn = sqlite3.connect("wages.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS state(
state TEXT NOT NULL
);''')


cur.execute('''CREATE TABLE IF NOT EXISTS counties(
state TEXT NOT NULL,
county TEXT NOT NULL,
date      TEXT     NOT NULL,
link      TEXT  NOT NULL,
FOREIGN KEY(state) REFERENCES state(state)
);''')

cur.execute("select state from state")

everything = cur.fetchall()
print("'AK'" in everything)
for i in everything:
    print("AK" in i)
    print(i)