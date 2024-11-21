import sqlite3
# make a table
def make_table():
    connection = sqlite3.connect("./my_db.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name VARCHAR (400) , lname VARCHAR (400) , password  VARCHAR (100)); "
    cursor.execute(sql)
    connection.commit()
    connection.close()
make_table()
# a function for inserting
def insert(username, lastname,password):
    connection = sqlite3.connect("./my_db.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (NULL , ? , ? , ?)" , (username,lastname,password))
    connection.commit()
    connection.close()
# a funtion for select
def select(username , lastname , password):
    connection = sqlite3.connect("./my_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE name=? and lname=? and password = ?",(username,lastname,password))
    res = cursor.fetchone()
    connection.commit()
    connection.close()
    return res
