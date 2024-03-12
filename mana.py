import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to select data from a table
cursor.execute('SELECT * FROM your_table')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Process the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
