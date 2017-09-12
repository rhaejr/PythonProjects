import sqlite3, json

conn = sqlite3.connect('wages.db')
cur = conn.cursor()

cur.execute('select * from counties')
db_json = {}
# extract column names
column_names = [d[0] for d in cur.description]

for row in cur:
    # build dict
    info = dict(zip(column_names, row))

    # dump it to a json string
    reply = json.dumps(info)
    name = info['state'] + info['county'] + str(info['date'])
    print(name)
