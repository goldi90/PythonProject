import connections
import css
def ShowAll():
    ShowContacts = connections.mydb.cursor()
    ShowContacts.execute("select * from contactno.contacts")
    for (NameOfPerson,ContactNO) in ShowContacts:
        print(NameOfPerson,ContactNO)
    connections.mydb.close()

def CreateContact():
    print(css.color.BOLD+"Note: You are creating Contact"+ css.color.END)
    personName= input("Enter The Name Of Person : ")
    Number=input("Enter The  number of Person : ")
    CreateContacts = connections.mydb.cursor()
    sql = "INSERT INTO contactno.contacts(NameOfPerson, ContactNo) VALUES (%s, %s)"
    val = ("{}".format(personName), "{}".format(Number))
    CreateContacts.execute(sql, val)
    connections.mydb.commit()
    print(CreateContacts.rowcount, "record inserted.")
    connections.mydb.close()
def UpdateContactNumber():
    Where=input("Enter the Name of contact You want to update : ")
    Value=input("value that You want to replace : ")
    UpdateContacts=connections.mydb.cursor()
    sql = "update contactno.contacts set ContactNo=(%s) where NameOfPerson=(%s)"
    val = ("{}".format(Value), "{}".format(Where))
    UpdateContacts.execute(sql,val)
    connections.mydb.commit()
    connections.mydb.close()
def UpdateContactName():
    Where=input("Enter the Number of contact You want to update : ")
    Value=input("value that You want to replace : ")
    UpdateContacts=connections.mydb.cursor()
    sql = "update contactno.contacts set NameOfPerson=(%s) where ContactNO=(%s)"
    val = ("{}".format(Value), "{}".format(Where))
    UpdateContacts.execute(sql,val)
    connections.mydb.commit()
    connections.mydb.close()
    
def DeleteRecordByNumber():
      Name= input("Enter The Number of Person YOu Want To delete")
      DeleteContacts=connections.mydb.cursor()
      sql="delete from contactno.contacts  where ContactNO=(%s)"
      val=(Name,)
      DeleteContacts.execute(sql,val)
      connections.mydb.commit()
      connections.mydb.close()

def DeleteRecord():
      Name= input("Enter The Name of Person YOu Want To delete")
      DeleteContacts=connections.mydb.cursor()
      sql="delete from contactno.contacts where NameOfPerson=(%s)"
      val=(Name,)
      DeleteContacts.execute(sql,val)
      connections.mydb.commit()
      connections.mydb.close()
