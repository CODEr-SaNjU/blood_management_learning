import sqlite3
connection = sqlite3.connect('blooddatabase.db')

cursor = connection.cursor()

def get_username_password(username,password):
    pass

def get_username(username):
    user =cursor.execute("SELECT * FROM Users where username=?",(username,))
    data = user.fetchone()
    if data:
        return False
    return True
    


def create_user(username, name,password,role):
    if create_user_table():
        data = (username, name,password,role)
        if get_username(username):
            sql = "INSERT INTO Users (username, name,password, role) VAlues (?, ?,?,?)"
            cursor.execute(sql, data)
            connection.commit()
            connection.close()
            return True
        else:
            print("username already exist")
    
    return False


def create_user_table():
    table_create = cursor.execute("""CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE, name TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL)""")
    #commit the chnages to the database
    connection.commit()

    return table_create

create_user('name', 'username','password','role')
