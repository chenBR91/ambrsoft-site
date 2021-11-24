from connection import connection

cursor = connection.cursor()

# queries for inserting value
insert = "INSERT INTO user(first_name, last_name, email) VALUES(%s, %s, %s)"

# add user to database
user = ('Lev', 'Jon', 'lev@gmail.vom')

# excuting the quires
cursor.execute(insert, user)


#commiting the connection then closing it.
connection.commit()
connection.close()
