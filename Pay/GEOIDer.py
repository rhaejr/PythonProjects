import csv, sqlite3

conn = sqlite3.connect('wages.db')
cur = conn.cursor()

cur.execute('select state, county from counties')
counties = cur.fetchall()

with open('GEOIDs.txt', 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)
test = []

for x in csv_list:
    geoid = str(x[1]) + str(x[2])
    cur.execute('update counties set GEOID = "{}" where state= "{}" and county="{}"'.format(geoid, x[0], x[3]))
    print(geoid)
conn.commit()