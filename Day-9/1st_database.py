import sqlite3

#create database

conn_string=sqlite3.connect('users.db')
cursor=conn_string.cursor()

#create table
create_table="CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, age INTEGER)"
cursor.execute(create_table)

#insert data
# cursor.execute("INSERT INTO user VALUES ('Sakib','open1234',25)")
# cursor.execute("INSERT INTO user VALUES ('Mijan','123456123',26)")
# cursor.execute("INSERT INTO user VALUES ('Abid','pen1234',55)")
# cursor.execute("INSERT INTO user VALUES ('Nabil','1234123',25)")
#conn_string.commit()

#delete data
cursor.execute("DELETE FROM user WHERE name='Abid'")
conn_string.commit()

#update data
# cursor.execute("UPDATE user SET age=36 WHERE age=26")
# conn_string.commit()