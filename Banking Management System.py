import mysql.connector as a
con=a.connect(host='localhost', user="root", password="12345", database="banking")

def openacc():
    cur=con.cursor()
    Name=input("Enter the Name:")
    Account_Number=input("Enter the Account Number:")
    Date_of_Birth=input("Enter the Date of Birth:")
    Phone_Number=input("Enter the phone number:")
    Address=input("Enter the Address:")
    Balance=int(input("Enter Opening Balance:"))
    s='insert into account values (%s, %s, %s, %s, %s, %s)'
    k='insert into amount values(%s, %s, %s)'
    s1='insert into account1 values(%s, %s, %s, %s,%s)'
    o=(Name, Account_Number, Date_of_Birth, Phone_Number, Address, Balance)
    v=(Name, Account_Number, Balance)
    o1=(Name, Account_Number, Date_of_Birth,Phone_Number, Address)
    cur.execute(s,o)
    cur.execute(k,v)
    cur.execute(s1,o1)
    con.commit()
    print("Data Entered Successfully")
    main()

def depoAmo():
    am=int(input("Enter Amount:"))
    Account_Number=input("Enter Account No:")
    a="select Balance from amount where Account_Number=%s"
    f1=(Account_Number,)
    c=con.cursor()
    c.execute(a,f1)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sl="update amount set Balance=%s where Account_Number=%s"
    d=(tam,Account_Number)
    c.execute(sl,d)
    con.commit()
    print("Successfully deposited")
    main()

def witham():
    am=int(input("Enter Amount:"))
    Account_Number=input("Enter Account No:")
    a="select Balance from amount where Account_Number=%s"
    data=(Account_Number,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sl="update amount set Balance=%s where Account_Number=%s"
    d=(tam,Account_Number)
    c.execute(sl,d)
    con.commit()
    print("Successfully withdrawn")
    main()

def balance():
    Account_Number=input("Enter Account Number:")
    a="select Balance from amount where Account_Number=%s"
    data=(Account_Number,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for Account Number:", Account_Number, "is", myresult[0])
    main()
def dispacc():
    Account_Number=input("Enter Account Number:")
    a="select * from account1 where Account_Number=%s"
    data=(Account_Number,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=" ")
    main()
def closeac():
    Account_Number=input("Enter Account Number:")
    sql1="delete from account where Account_Number=%s"
    sql2="delete from amount where Account_Number=%s"
    sql3="delete from account1 where Account_Number=%s"
    data=(Account_Number,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2, data)
    c.execute(sql3, data)
    con.commit()
    print("Successfully Closed")
    main()
def main():
    print("""
    1. OPENING NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY THE CUSTOMER DETAILS
    6. CLOSE AN ACCOUNT
    """)
    choice=input("Enter Task Number:")
    if(choice == '1'):
        openacc()
    elif(choice == '2'):
        depoAmo()
    elif (choice == '3'):
        witham()
    elif(choice == '4'):
        balance()
    elif(choice == '5'):
        dispacc()
    elif(choice == '6'):
        closeac()
    else:
        print("Wrong choice. ......")
        main()
main()
