import sqlite3
# make a table
class sqlite:
    def __init__(self , username , lastname , password):
        self.username = username
        self.lastname = lastname
        self.password = password
    def make_table(self):
        connection = sqlite3.connect("./my_db.db")
        cursor = connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name VARCHAR (400) , lname VARCHAR (400) , password  VARCHAR (100)); "
        cursor.execute(sql)
        connection.commit()
        connection.close()
    # a function for inserting
    def insert(self):
        connection = sqlite3.connect("./my_db.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES (NULL , ? , ? , ?)" , (self.username,self.lastname,self.password))
        connection.commit()
        connection.close()
    # a funtion for select
    def select(self):
        connection = sqlite3.connect("./my_db.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name=? and lname=? and password = ?",(self.username,self.lastname,self.password))
        res = cursor.fetchone()
        connection.commit()
        connection.close()
        return res