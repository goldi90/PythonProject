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
    ShowContacts = mydb.cursor()
    ShowContacts.execute("select * from contactno.contacts")
    for (NameOfPerson,ContactNO) in ShowContacts:
        print(NameOfPerson,ContactNO)
    mydb.close()

def CreateContact():
    print(css.color.BOLD+"Note: You are creating Contact"+ css.color.END)
    personName= input("Enter The Name Of Person : ")
    Number=input("Enter The  number of Person : ")
    CreateContacts = mydb.cursor()
    sql = "INSERT INTO contactno.contacts(NameOfPerson, ContactNo) VALUES (%s, %s)"
    val = ("{}".format(personName), "{}".format(Number))
    CreateContacts.execute(sql, val)
    mydb.commit()
    print(CreateContacts.rowcount, "record inserted.")
    mydb.close()
def UpdateContactNumber():
    Where=input("Enter the Name of contact You want to update : ")
    Value=input("value that You want to replace : ")
    UpdateContacts=mydb.cursor()
    sql = "update contactno.contacts set ContactNo=(%s) where NameOfPerson=(%s)"
    val = ("{}".format(Value), "{}".format(Where))
    UpdateContacts.execute(sql,val)
    mydb.commit()
    mydb.close()
def UpdateContactName():
    Where=input("Enter the Number of contact You want to update : ")
    Value=input("value that You want to replace : ")
    UpdateContacts=mydb.cursor()
    sql = "update contactno.contacts set NameOfPerson=(%s) where ContactNO=(%s)"
    val = ("{}".format(Value), "{}".format(Where))
    UpdateContacts.execute(sql,val)
    mydb.commit()
    mydb.close()
    
def DeleteRecord():
      Name= input("Enter The Name of Person YOu Want To delete")
      DeleteContacts=mydb.cursor()
      sql="delete from contactno.contacts  where NameOfPerson=(%s)"
      val=("{}".format(Name))
      DeleteContacts.execute(sql,val)
      mydb.commit()
      mydb.close()
def DeleteRecordByNumber():
      Name= input("Enter The Number of Person YOu Want To delete")
      DeleteContacts=mydb.cursor()
      sql="delete from contactno.contacts  where ContactNO=(%s)"
      val=("{}".format(Name))
      DeleteContacts.execute(sql,val)
      mydb.commit()
      mydb.close()

Action=input('\033[94m'+'\033[1m'+"Press C for Creating contact:\nPress A for get all Contact :\nPress UN To update Number   :  \nPress UP To update Name Of person   : "+css.color.END +'\033[91m'+'\033[1m'+"\nPress D To delete Contact   :  \nPress DN To delete Contact By Number   :  "+css.color.END )
if Action=="c" or Action=="C":
    CreateContact()
if Action=="a" or Action=="A":
    ShowAll()
if Action=="un" or Action=="UN":
    UpdateContactNumber()
if Action =="UP" or Action=="up":
     UpdateContactName()   
if Action =="d" or Action=="D":
    DeleteRecord()
if Action =="DN" or Action =="dn":
    DeleteRecordByNumber()