import requests, csv, os
import sqlite3

conn = sqlite3.connect("wages - Copy.db")
cur = conn.cursor()

# page = 'AF Wage Schedules96.html'
# page2 = 'AF Schedule Area 077R Northern Mississippi (RUS) Effective_ 17 April 2016.html'
#'AF Schedule Area 124R Memphis, Tennessee (RUS) Effective_ 17 April 2016.html'


def table_parser(page):
    file = open(page)
    # page = page.split('\n')
    table = []
    num = 0
    for line in file:
        if 'Grade' in line:
            num += 1
        if num > 0:
            num += 1
        if 3 <= num < 21:
            line = line.rstrip()
            if line != '':
                split_line = line.split(' ')
                split_line = [x for x in split_line if x != '']
                strip_line = split_line[:16]
                table.append(strip_line)
    WG = []
    WL = []
    WS = []
    for l in table:
    # WG.append(l[0:1])
    # WL.append(l[0:1])
    # WS.append(l[0:1])
        WG.append((l[1:6]))
        WL.append(l[6:11])
        WS.append(l[11:16])

    file.close()
    return WG, WL, WS

cur.execute('select link from counties where county="150,150,RUS,Washakie County" and date="12Mar1996"')
link = cur.fetchall()[0][0]

res = requests.get(link,verify=False)
html = res.text
os.makedirs('test/test', exist_ok=True)
file = open('test/test.html','w')
for line in html:
    line = line.strip('\n')
    file.write(line)
file.close()

data = table_parser('test.html')


with open('test_wg.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data[0])
with open('test_wl.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data[1])
with open('test_ws.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data[2])

