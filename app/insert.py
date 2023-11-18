import psycopg2

conn = psycopg2.connect(
    host="db",
    database="flask_db",
    user="postgres",
    password="password"
)

cur = conn.cursor()
conn.autocommit = True

# Insert data into the table
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

print("Data inserted successfully, {} rows.".format(cur.rowcount)) # of rows affected by the command

cur.close()
conn.close()
