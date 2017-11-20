import sqlite3

def createTable():
    connection = sqlite3.connect("data.db")
    #connection.execute("CREATE TABLE USERS(USERNAME NOT NULL,PASSWORD TEXT,EMAIL TEXT) ")
    #connection.execute("CREATE TABLE USERINFO3(FIRST TEXT, LAST TEXT, DOB TEXT, AGE INTEGER, CITY TEXT, HOBBIES TEXT, QUALIFICATION TEXT, PROFESSION TEXT)")
    connection.commit()
    # result = connection.execute("SELECT * FROM USERS")
    # for data in result:
    #     print("Username : ",data[0])
    #     print("Password : ", data[1])
    #     print("Email : ", data[2])

    result = connection.execute("SELECT * FROM USERINFO3")
    for data in result:
        print("First: ", data[0])
        print("Last: ", data[1])
        print("DOB: ", data[2])
    connection.close()
createTable()