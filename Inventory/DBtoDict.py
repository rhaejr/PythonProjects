import sqlite3, json, pickle

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

cur.execute('select * from benchstock')
db_json = {}
# extract column names
column_names = [d[0] for d in cur.description]

for row in cur:
    # build dict
    info = dict(zip(column_names, row))

    # dump it to a json string
    # reply = json.dumps(info)
    name = info['nsn']
    db_json[name] = info


with open('db.p', 'wb') as outfile:
    pickle.dump(db_json, outfile)