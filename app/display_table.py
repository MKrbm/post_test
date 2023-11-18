
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="db",
    database="flask_db",
    user="postgres",
    password="password"
)

cur = conn.cursor()
conn.autocommit = True

# Select data from the table
cur.execute('SELECT * FROM books;')
# fetchall() retrieves all rows of a query result and store in dataframe
rows = cur.fetchall()
columns = [desc[0] for desc in cur.description]
df = pd.DataFrame(rows, columns=columns)

print(df)

cur.close()
conn.close()
