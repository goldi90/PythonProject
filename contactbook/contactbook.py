from os import name
import css
import mysql.connector as connector
mydb = connector.connect(
  host="127.0.0.1",
  user="kaushik1",
  password="123"
  )

# print(mydb)
def ShowAll():
    mycursor = mydb.cursor()
    mycursor.execute("select * from contactno.contacts")
    for (NameOfPerson,ContactNO) in mycursor:
        print(NameOfPerson,ContactNO)
    # mydb.close()

def CreateContact():
    print(css.color.BOLD+"Note: You are creating Contact"+ css.color.END)
    personName= input()
    Number=input()
    mycursor = mydb.cursor()
    sql = "INSERT INTO contactno.contacts(NameOfPerson, ContactNo) VALUES (%s, %s)"
    val = ("{}".format(personName), "{}".format(Number))
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close()
ShowAll()
CreateContact()
