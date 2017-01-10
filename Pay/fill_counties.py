import sqlite3

conn = sqlite3.connect('wages.db')
cur = conn.cursor()

cur.execute("SELECT * FROM counties where county is null")
x = cur.fetchall()
for i in x:
    info = i[1].split(',')
    # cur.execute('update counties set county="{}" where county_info="{}"'.format(info[3], i[1]))
    # conn.commit()


    print(info[3])
print(len(x))
conn.close()