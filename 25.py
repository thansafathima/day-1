# Database
# resource containing datadata - info
# classified into two
# 1.relational Database
# data table format
# language : sql
# eg:Mysql,posgresq1,sqllite
# 2.non relational Database
# file based or record based
# eg:mongo db


import sqlite3
conn = sqlite3.connect("first.db")   #establshing a connection to the db
cursor = conn.cursor() #to interact with the database

#operations
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Student(
        name VARCHAR(20),
        age INTEGER,
        address TEXT
        )
    '''
)

def addstudent():
    conn = sqlite3.connect("first.db")  #establishing a connection to the db
cursor = conn.cursor()
student_name = input("enter student name :- ")
student_age = int(input("enter student age :-"))
student_address = input("enter student address")
cursor.execute('''
    INSERT INTO Student(name,age,address)
            VALUES(?,?,?)
    
    ''', (student_name, student_age,student_address))
conn.commit()
print("student added ")

conn.close()


def main():
    while True:
        print("welcome to student management")
        ch = int(input("1.ADD STUDENT\n2.VIEW STUDENT"))
        if ch == 1:
            addstudent()
        else:
            print("invalid choice")

main()
