import psycopg2

conn = psycopg2.connect(
    host="db",
    database="flask_db",
    user="postgres",
    password="password"
)

# Open a cursor to perform database operations
cur = conn.cursor()
# auto commit each transaction
conn.autocommit = True

# Execute a command: this creates a new table
# cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE IF NOT EXISTS books ('
            'id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'pages_num integer NOT NULL,'
            'review text,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )
print("Table created successfully, {} rows.".format(cur.rowcount))


cur.close()
conn.close()
