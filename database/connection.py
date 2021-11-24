import pymysql

# database connection
dbhost = 'localhost'
dbuser = 'root'
dbpass = ''
dbname= 'users'

connection = pymysql.connect(host = dbhost, user = dbuser, passwd = dbpass, database = dbname)

