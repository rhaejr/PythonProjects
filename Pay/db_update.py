import csv, sqlite3, re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def csv_list(file):
    with open(file, 'r', ) as f:
        reader = csv.reader(f)
        list_csv = list(reader)

    return list_csv

conn = sqlite3.connect('wages.db')
cur = conn.cursor()
grades = ['wg1', 'wg2', 'wg3', 'wg4', 'wg5', 'wg6', 'wg7', 'wg8', 'wg9', 'wg10', 'wg11', 'wg12', 'wg13', 'wg14', 'wg15', 'wl1', 'wl2', 'wl3', 'wl4', 'wl5', 'wl6', 'wl7', 'wl8', 'wl9', 'wl10', 'wl11', 'wl12', 'wl13', 'wl14', 'wl15', 'ws1', 'ws2', 'ws3', 'ws4', 'ws5', 'ws6', 'ws7', 'ws8', 'ws9', 'ws10', 'ws11', 'ws12', 'ws13', 'ws14', 'ws15']
# for i in [['wg1', 'real'],['wg2', 'real'],['wg3', 'real'],['wg4', 'real'],['wg5', 'real'],['wg6', 'real'],['wg7', 'real'],['wg8', 'real'],['wg9', 'real'],['wg10', 'real'],['wg11', 'real'],['wg12', 'real'],['wg13', 'real'],['wg14', 'real'],['wg15', 'real'],['wl1', 'real'],['wl2', 'real'],['wl3', 'real'],['wl4', 'real'],['wl5', 'real'],['wl6', 'real'],['wl7', 'real'],['wl8', 'real'],['wl9', 'real'],['wl10', 'real'],['wl11', 'real'],['wl12', 'real'],['wl13', 'real'],['wl14', 'real'],['wl15', 'real'],['ws1', 'real'],['ws2', 'real'],['ws3', 'real'],['ws4', 'real'],['ws5', 'real'],['ws6', 'real'],['ws7', 'real'],['ws8', 'real'],['ws9', 'real'],['ws10', 'real'],['ws11', 'real'],['ws12', 'real'],['ws13', 'real'],['ws14', 'real'],['ws15', 'real']]:
#     cur.execute('alter table counties add column {} {}'.format(i[0],i[1]))
select = cur.execute('select wg, ws, wl, state, county, date from counties where wl1 is NULL').fetchall()
for i in select:
    state = i[3]
    county = i[4]
    date = i[5]
    try:
        # print(i[0])
        wg = csv_list(i[0])
        cur.execute('update counties set wg1="{}", wg2="{}", wg3="{}", wg4="{}", wg5="{}", wg6="{}", wg7="{}", wg8="{}", wg9="{}", wg10="{}", wg11="{}", wg12="{}", wg13="{}", wg14="{}", wg15="{}" where wg ="{}"'.format(wg[0][4],wg[1][4],wg[2][4],wg[3][4],wg[4][4],wg[5][4],wg[6][4],wg[7][4],wg[8][4],wg[9][4],wg[10][4],wg[11][4],wg[12][4],wg[13][4],wg[14][4],i[0]))

        wl = csv_list(i[1])

        print(i[1])
        # print(cur.execute('select * from counties where wl="{}"'.format(i[1])).fetchall())
        cur.execute(
            'update counties set wl1="{}", wl2="{}", wl3="{}", wl4="{}", wl5="{}", wl6="{}", wl7="{}", wl8="{}", wl9="{}", wl10="{}", wl11="{}", wl12="{}", wl13="{}", wl14="{}", wl15="{}" where state ="{}" and county ="{}" and date ="{}"'.format(
                wl[0][4], wl[1][4], wl[2][4], wl[3][4], wl[4][4], wl[5][4], wl[6][4], wl[7][4], wl[8][4], wl[9][4],
                wl[10][4], wl[11][4], wl[12][4], wl[13][4], wl[14][4], state, county, date))
        # print(cur.execute('select wl, wl1 from counties where wl="{}"'.format(i[1])).fetchall())
        ws = csv_list(i[2])
        cur.execute(
            'update counties set ws1="{}", ws2="{}", ws3="{}", ws4="{}", ws5="{}", ws6="{}", ws7="{}", ws8="{}", ws9="{}", ws10="{}", ws11="{}", ws12="{}", ws13="{}", ws14="{}", ws15="{}" where state ="{}" and county ="{}" and date ="{}"'.format(
                ws[0][4], ws[1][4], ws[2][4], ws[3][4], ws[4][4], ws[5][4], ws[6][4], ws[7][4], ws[8][4], ws[9][4],
                ws[10][4], ws[11][4], ws[12][4], ws[13][4], ws[14][4], state, county , date))
    except IndexError:
        cur.execute('update counties set verified="Index" where wg="{}"'.format(i[0]))
        print('index {}'.format(i[0]))

    # except KeyboardInterrupt:
    #     print(i[0])

        
    conn.commit()
conn.close()