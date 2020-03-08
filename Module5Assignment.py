import sqlite3
import sqlite3 as lite
import os
import sys

print('Question 1:\n')

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    # Code change xxxxx > sqlite_version();
    cur.execute('SELECT sqlite_version();')
    data = cur.fetchone()

print "SQLite version: %s" % data

print('\nQuestion 2:\n')

con = sqlite3.connect('new_db')
with con:
    cur = con.cursor()
    # cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    # cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

    # Added the following code to debug
    cur.execute("SELECT Id FROM Friends ORDER BY Id DESC LIMIT 1;")
    data = cur.fetchone()

    # Changed % > % data
    print ("The last Id of the inserted row is %d" % data)

print('\nQuestion 3:\n')

db_filename = 'todo.db'

# Changed XXXX > os.path.isfile
db_is_new = not os.path.isfile(db_filename)
conn = sqlite3.connect(db_filename)

if db_is_new:
    print 'Need to create schema'
    print 'Creating database'
else:
    print 'Database exists, assume schema does, too.'

print('\nQuestion 4:\n')

con = sqlite3.connect('test_db')

with con:
    cur = con.cursor()
    # cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name TEXT);")
    # cur.execute("INSERT INTO Cars(Name) VALUES ('Aston');")
    # cur.execute("INSERT INTO Cars(Name) VALUES ('Ferrari');")
    # cur.execute("INSERT INTO Cars(Name) VALUES ('Pagani');")
    # cur.execute("INSERT INTO Cars(Name) VALUES ('McClaren');")

    # Changed SELECT * FROM Cars > PRAGMA table_info(Cars)
    cur.execute("PRAGMA table_info(Cars)")

    # Changed XXXX > fetchall()
    for colinfo in cur.fetchall():
        print colinfo

print('\nQuestion 5:\n')

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600))

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    for car in cars:
        cur.execute("INSERT INTO Cars VALUES(?, ?, ?)", car)
    print ('Table Cars created and populated.')

print('\nQuestion 6:\n')

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print row

print('\nQuestion 7:\n')

con = lite.connect('test.db')
with con:
    # Changed XXX > Row
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])

print('\nQuestion 8:\n')

uId = 1
uPrice = 62300
con = lite.connect('test.db')
with con:
    cur = con.cursor()
    # Changed X,Y > uPrice, uId
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
    con.commit()
    cur.execute("SELECT * FROM Cars WHERE Id = ?", (uId,))
    row = cur.fetchall()
    print (row)
    print "Number of rows updated: %d" % cur.rowcount

print('\nQuestion 9:\n')

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('PRAGMA table_info(Cars)')
    data = cur.fetchall()
    for d in data:
        print d[0], d[1], d[2]

print('\nQuestion 10:\n')

con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print ("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))
    for row in rows:
        print "%2s %-10s %s" % row
