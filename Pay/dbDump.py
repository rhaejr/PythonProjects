import sqlite3, json, pickle

conn = sqlite3.connect('wages.db')
cur = conn.cursor()

cur.execute('select * from counties')
db_json = {}
# extract column names
column_names = [d[0] for d in cur.description]
i = 0
for row in cur:
    # build dict
    info = dict(zip(column_names, row))

    # dump it to a json string
    # reply = json.dumps(info)
    # name = str(i)
    print(i)
    i += 1
    db_json[str(i)] = info

with open('test.json', 'w') as outfile:
    json.dump(db_json, outfile)