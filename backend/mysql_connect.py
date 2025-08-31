import mysql.connector

cnx = mysql.connector.connect(user='root', password='Qwerty@123',
                              host='127.0.0.1',
                              database='grocery_store')
cnx.close()
[]