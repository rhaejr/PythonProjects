import sqlite3

conn = sqlite3.connect('wages.db')
cur = conn.cursor()
year = '2016'
grade = 'wg10'


cur.execute('select {} from counties where date like "%{}%"'.format(grade, year))
pay = cur.fetchall()
pay_list = []

for i in pay:
    pay_list.append(i[0])
print(len(pay_list))
pay_list = list(filter(None, pay_list))
print(len(pay_list))
print(sum(pay_list)/len(pay_list))


