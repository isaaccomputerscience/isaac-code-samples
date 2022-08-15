# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0
#
# Requires users.db (sqlite database) to be in same folder as script


import sqlite3

def attempt_login(userid, pword):
    try: 
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        sql = f"SELECT * FROM passwords where userid = '{userid}' AND password = '{pword}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) == 1:
            print("Success - you are logged in")
        else:
            print("Access denied")
    except:
        print ("Failed to connect to database")

def normal_login():
    userid = input("Enter your userid: ")  
    pword = input("Enter your password: ") 
    attempt_login(userid, pword)

def hack_that_db():
    userid = "x"
    pword = "x' OR 1=1 LIMIT 1 --"
    attempt_login(userid, pword)

    



if __name__ == "__main__":
    normal_login()
    #hack_that_db()
