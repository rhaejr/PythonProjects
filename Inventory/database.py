import sqlite3, csv

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS benchstock(
nsn TEXT     NOT NULL,
pn    TEXT ,
desc    TEXT ,
remarks    TEXT ,
location TEXT ,
niin TEXT,
acft TEXT
);''')



with open('inventory.csv', 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)

for i in csv_list:
    try:
        cur.execute('insert into benchstock values(?,"",?,?,?,?,"apache")', (i[1], i[2], i[3], i[0], i[1][4:]))
    except:
        print(i)

conn.commit()
conn.close()