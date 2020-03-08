import csv
import sqlite3 as lite


    # csv_reader = csv.reader(csv_file, delimiter=',')
    # line_count = 0
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')
with open('sample-storedata.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    con = lite.connect('store.db')

    with con:
        cur = con.cursor()
        #cur.execute("CREATE TABLE CustDetails(Latitude REAL, Longitude REAL, Phone TEXT, Address TEXT);")
        for row in csv_reader:
            cur.execute("INSERT INTO CustDetails VALUES(?, ?, ?, ?)", row)

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM CustDetails")

    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print ("%s %-10s %s %s" % (col_names[0], col_names[1], col_names[2], col_names[3]))
    for row in rows:
        print ("%2s %-10s %s %s" % row)
