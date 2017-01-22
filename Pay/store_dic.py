import sqlite3, pickle, csv


def csv_list(file):
    with open(file, 'r', ) as f:
        reader = csv.reader(f)
        list_csv = list(reader)

    return list_csv


conn = sqlite3.connect('wages.db')
cur = conn.cursor()
with open("database_dict.p", "rb") as f:
    database = pickle.load(f)
# database = pickle.load(open("database_dict.p", "rb"))
# for i in select:
#     state = i[0]
#     county = i[1]
#     date = i[2]
#     wg = i[3]
#     wl = i[4]
#     ws = i[5]
#     county_info = i[6]
#     if state not in database:
#         database[state] = {}
#     if county not in database[state]:
#         database[state][county] = {}
#     if date not in database[state][county]:
#         database[state][county][date] = {}
#     if 'wg' not in database[state][county][date]:
#         database[state][county][date]['wg'] = {}
#         database[state][county][date]['wl'] = {}
#         database[state][county][date]['ws'] = {}


select = cur.execute('select state, county, date, wg, wl , ws, county_info  from counties').fetchall()

for i in select:

    state = i[0]
    county = i[1]
    date = i[2]
    wg = i[3]
    wl = i[4]
    ws = i[5]
    county_info = i[6]

    print(len(database[state][county][date]['wg']))
    if len(database[state][county][date]['wg']) == 0:
        database[state][county][date]['wg'] = csv_list(wg)
        database[state][county][date]['wl'] = csv_list(wl)
        database[state][county][date]['ws'] = csv_list(ws)
        print(ws)

    else:
        print('fail')

with open("database_dict.p", "wb") as f:
    pickle.dump(database, f)
conn.close()
