from os import name
import css
import Function
# Nedd To Update
Action=input('\033[94m'+'\033[1m'+"Press C for Creating contact:\nPress A for get all Contact :\nPress UN To update Number   :  \nPress UP To update Name Of person   : "+css.color.END +'\033[91m'+'\033[1m'+"\nPress D To delete Contact   :  \nPress DN To delete Contact By Number   :  "+css.color.END )
if Action=="c" or Action=="C":
    Function.CreateContact()
if Action=="a" or Action=="A":
    Function.ShowAll()
if Action=="un" or Action=="UN":
    Function.UpdateContactNumber()
if Action =="UP" or Action=="up":
    Function.UpdateContactName()   
if Action =="d" or Action=="D":
    Function.DeleteRecord()
if Action =="DN" or Action =="dn":
    Function.DeleteRecordByNumber()

