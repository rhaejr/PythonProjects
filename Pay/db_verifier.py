import sqlite3

conn = sqlite3.connect("wages.db")
cur = conn.cursor()

grades = ['wg1', 'wg2', 'wg3', 'wg4', 'wg5', 'wg6', 'wg7', 'wg8', 'wg9', 'wg10', 'wg11', 'wg12', 'wg13', 'wg14', 'wg15',
          'wl1', 'wl2', 'wl3', 'wl4', 'wl5', 'wl6', 'wl7', 'wl8', 'wl9', 'wl10', 'wl11', 'wl12', 'wl13', 'wl14', 'wl15',
          'ws1', 'ws2', 'ws3', 'ws4', 'ws5', 'ws6', 'ws7', 'ws8', 'ws9', 'ws10', 'ws11', 'ws12', 'ws13', 'ws14', 'ws15']

for i in grades:
    cur.execute('select count(*) from counties where {} is null'.format(i))
    print('{} {}'.format(i, cur.fetchall()[0][0]))

conn.close()