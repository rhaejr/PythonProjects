import smtplib
from datetime import datetime
import requests, csv, sqlite3, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
not_done = True
while not_done:
    try:
        conn = sqlite3.connect("wages.db")
        cur = conn.cursor()

        cur.execute('select state, county, date, link from counties where verified="Grade"')
        for row in cur.fetchall():
            state = row[0]
            county = row[1]
            date = row[2]
            res = requests.get(row[3], verify=False,)
            html = res.text
            os.makedirs('docs/{}/{}/{}'.format(state, county, date), exist_ok=True)
            file = open('docs/{}/{}/{}/{}-{}-{}.html'.format(state, county, date, state, county, date), 'w')
            for line in html:
                # line = line.strip('\n')
                file.write(line)
            file.close()

            data = table_parser('docs/{}/{}/{}/{}-{}-{}.html'.format(state, county, date, state, county, date))

            wg = 'docs/{}/{}/{}/{}-{}-{}_wg.csv'.format(state, county, date, state, county, date)
            wl = 'docs/{}/{}/{}/{}-{}-{}_wl.csv'.format(state, county, date, state, county, date)
            ws = 'docs/{}/{}/{}/{}-{}-{}_ws.csv'.format(state, county, date, state, county, date)

            with open(wg, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data[0])
            with open(wl, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data[1])
            with open(ws, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data[2])

                cur.execute(
                    'update counties set wg="{}", wl="{}", ws="{}" where state="{}" and county="{}" and date="{}"'.format(wg,
                                                                                                                            wl,
                                                                                                                            ws,
                                                                                                                            state,
                                                                                                                            county,
                                                                                                                            date))
                print("{} {} {}".format(state, county, date))
                conn.commit()
        conn.close()
        not_done = False
    except:
        conn = sqlite3.connect("wages.db")
        cur = conn.cursor()
        cur.execute("select * from counties where wg not NULL")
        everything = cur.fetchall()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('av8r.08@gmail.com', '1111aasfULLS$$')
        server.sendmail('av8r.08@gmail.com', '6623466983@vtext.com', 'Code Stopped!\n{}\n{}'.format(
            len(everything),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.close()