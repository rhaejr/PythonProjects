import csv, sqlite3, re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


conn = sqlite3.connect('testwages.db')
cur = conn.cursor()
try:
    cur.execute('alter table counties add column verified text')
except sqlite3.OperationalError:
    pass

select = cur.execute('select * from counties where verified="Grade"').fetchall()
for i in select:
    # print(i)
    state = i[0]
    county = i[1]
    date = i[2]
    file = open('docs/NY/097,097,RUS,Madison County/26Apr1996/NY-097,097,RUS,Madison County-26Apr1996.html','r')
    file = open('docs/{}/{}/{}/{}-{}-{}.html'.format(state, county, date, state, county, date), 'r')
    for line in file:
        if '404 - File or directory not found' in line:
            print('404')
            cur.execute('update counties set verified="404" where state="{}" and county="{}" and date="{}"'.format(state,county, date))

# select = cur.execute('select wg, wl, ws from counties where verified is NULL').fetchall()
#
# for i in select:
#     verified = False
#     for file in i:
#         print(file)
#         with open(file, 'r',) as f:
#             reader = csv.reader(f)
#             csv_list = list(reader)
#             if len(csv_list) == 15:
#                 for row in csv_list:
#                     if len(row) == 5:
#                         row = [cleanhtml(x) for x in row]
#                         try:
#                             row = [float(x) for x in row]
#                         except ValueError:
#                             cur.execute(
#                                 'update counties set verified="Float" where wg="{}" or wl="{}" or ws="{}"'.format(file,
#                                                                                                                 file,
#                                                                                                                 file))
#                         # everything past here should be at least 15 grades and 5 steps
#
#                     else:
#                         cur.execute(
#                             'update counties set verified="Step" where wg="{}" or wl="{}" or ws="{}"'.format(file, file,
#                                                                                                              file))
#             else:
#                 cur.execute('update counties set verified="Grade" where wg="{}" or wl="{}" or ws="{}"'.format(file, file, file))
#     conn.commit()



conn.close()
