from connection import connection

cursor = connection.cursor()


# queries for retrievint all rows
retrive = "SELECT * FROM user;"

# executing the quires
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
   print(row)


# commiting the connection then closing it.
connection.commit()
connection.close()