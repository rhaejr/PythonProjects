import sqlite3

conn = sqlite3.connect("wages.db")
cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS state(
# state TEXT NOT NULL
# );''')
#
#
# cur.execute('''CREATE TABLE IF NOT EXISTS counties(
# state TEXT NOT NULL,
# county TEXT NOT NULL,
# date      TEXT     NOT NULL,
# link      TEXT  NOT NULL,
# wg TEXT,
# wl TEXT,
# ws TEXT,
# FOREIGN KEY(state) REFERENCES state(state)
# );''')
# for i in [['wg', 'TEXT'],['wl', 'TEXT'],['ws', 'TEXT']]:
#     cur.execute('alter table counties add column {} {}'.format(i[0],i[1]))


cur.execute("select * from counties where wg not NULL")
everything = cur.fetchall()
# print("'AK'" in everything)
# for i in everything:
#     # print("AK" in i)
#     print(i)
print(len(everything))
print(everything[-1])

print(cur.execute("SELECT count(*) FROM counties").fetchall()[0][0])

# import smtplib
#
# server = smtplib.SMTP( "smtp.gmail.com", 587 )
# server.starttls()
# server.login( 'av8r.08@gmail.com', '1111aasfULLS$$' )
# server.sendmail( 'av8r.08@gmail.com', '6623466983@vtext.com', 'Code Stopped!' )
