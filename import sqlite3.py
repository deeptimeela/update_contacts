import sqlite3

mydb = sqlite3.connect("phonebook.db")
cur = mydb.cursor()
create_table = "CREATE TABLE if not exists phone_table12(name varchar(20), number int(10), email varchar(30),address varchar(60))"
cur.execute(create_table)

def input_data():
    name = input("Please enter the NAME:\n")
    number = input("Please enter the 10 DIGIT MOBILE NUMBER:\n")
    email= input("Please enter the EMAIL ID:\n")
    address= input("Please enter the ADDRESS:\n")

    data_insert = "insert into phone_table12(name,number,email,address) values(?,?,?,?)"
    data=(name,number,email,address)
    cur.execute(data_insert,data)
    mydb.commit()
    print("KUDOS,details saved SUCCESSFULLY!!")

def no_check():
    name = input("Please enter NAME of saved person who's DEATILS you want :\n")
    data_fetch = """select * from phone_table12 where name = ?"""
    cur.execute(data_fetch,(name,))
    result = cur.fetchall()
    for row in result:
        if(row[0]==name):
            print(row[1],"\n", row[2],"\n", row[3])
            

def update_recordnum():
    nm = input("Please enter NAME of user who's CONTACT you want to update:\n")
    newno = input("please enter new number\n")
    data_update = "UPDATE phone_table12 set number = ? where name = ?"
    values=(newno,nm)
    cur.execute(data_update,values)
    mydb.commit()
    print("KUDOS,Record has been Updated!!")

def delete_record():
    nm = input("Please enter NAME:\n")
    data_delete = "DELETE from phone_table12 where name = ?"
    cur.execute(data_delete,(nm,))
    mydb.commit()
    print("Record has been  deleted!")

def update_recordemail():
    nm = input("Please enter NAME of user who's EMAILID you want to update:\n")
    newmail = input("Please enter new EMAIL-ID\n")
    data_update = "UPDATE phone_table12 set email = ? where name = ?"
    values=(newmail,nm)
    cur.execute(data_update,values)
    mydb.commit()
    print("KUDOS,email id has been successfully Updated!")

def update_recordaddress():
    nm = input("Please enter name of user who's ADDRESS you want to update:\n")
    newadd = input("please enter new address\n")
    data_update = "UPDATE phone_table12 set address = ? where name = ?"
    values=(newadd,nm)
    cur.execute(data_update,values)
    mydb.commit()
    print("KUDOS,Address has been successfully Updated!")

def update_alphabetically():
   

    sql="SELECT * FROM phone_table12 ORDER BY name"
    cur.execute(sql)
    myresult=cur.fetchall()
    for x in myresult:
        print(x)
    




while True:
    x=input("1>--NEW RECORD ENTER\n2>--CHECK DETAILS BY NAME\n3>--UPDATE PHONE NUMBER\n4>--UPDATE EMAIL\n5>--UPDATE ADDRESS\n6>--UPDATE ALPHABETICALLY\n7>--DELETE RECORD")
    if x =='1':
        input_data()
    elif x == '2':
        no_check()
    elif x == '3':
        update_recordnum()
    elif x == '7':
        delete_record()
    elif x == '4':
        update_recordemail()
    elif x == '5':
        update_recordaddress()
    elif x == '6':
        update_alphabetically()

    else:
        print("quiting")
        break