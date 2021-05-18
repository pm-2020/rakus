import sqlite3
con = sqlite3.connect('chat.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE test3
               (text, text2)''')

# Insert a row of data
cur.execute("INSERT INTO test3 VALUES ('2006-01-05','BUY')")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

