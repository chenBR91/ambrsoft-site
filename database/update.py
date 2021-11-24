from connection import connection

cursor = connection.cursor()


updateSql = "UPDATE user SET first_name = 'Aviv' WHERE ID='4' ;"
cursor.execute(updateSql)


#commiting the connection then closing it.
connection.commit()
connection.close()