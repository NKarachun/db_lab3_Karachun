import json
import psycopg2

username = 'StudentKarachunA'
password = '2003'
database = 'db_lab2_Karachun'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()

    for table in ('wines', 'provinces', 'testers', 'countries'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('Karachun_DB_lab3.json', 'w') as outf:
    json.dump(data, outf, default=str, indent=4)