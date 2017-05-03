import sqlite3
from mytools import calculate_checksum
conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

select = cur.execute('select nsn from benchstock where acft="apache"').fetchall()
for i in select:
    if i[0].isdigit():
        code = '{}{}'.format('640', i[0][-9:])
        barcode = '{}{}'.format(str(code), str(calculate_checksum(code)))
        print('{} : {}'.format(i[0], barcode))

        cur.execute('update benchstock set barcode = "{}" where nsn="{}"'.format(barcode, i[0]))
conn.commit()
conn.close()