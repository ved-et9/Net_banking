import mysql.connector as c
import functions as f
import random
import re
import smtplib

mydb=c.connect(host="localhost",user="root",passwd="2002",database="net_banking")


cursorobejct= mydb.cursor()


#new account#

QRY=""" SELECT client_id FROM client"""




#functions#

def check(id):
    cursorobejct.execute(f.CHECK_ID)
    d=cursorobejct.fetchall()
    list_of_ids = []
    for x in d:
        
        list_of_ids.append(x[0])
         
    
    
    

    for x in range(0,len(list_of_ids)):
        if id==list_of_ids[x]:
            print("ALREADY REGISTERED PLEASE LOGIN WITH YOUR CORRECT CREDENTIALS")
            return 1
        else:
            continue
    
            
           
#new log in function#   

def new_login(adhaar,account_no,passw,fname,lname,email,mobile_no):
    
    

     cursorobejct.execute(f.NEW_LOGIN,(adhaar,account_no,passw,fname,lname,email,mobile_no))
     cursorobejct.execute(f.NEW_LOGIN_ACCOUNT,(adhaar,0,0))
     mydb.commit()



#client home screen#

def client_home(acc):
    cursorobejct.execute(f.FETCH_CLIENT_DETAILS,(acc,))
    q=cursorobejct.fetchall()
    
    
    print(f'------------Welcome {q[0][3]} {q[0][4]}\n\n')
    print(f.CLIENT_HOME)
    return int(input("\n-----Enter Your Choice: "))

#already client log in#

def user(acc_no,passw):
    
    cursorobejct.execute(f.CHECK__ACC)
    y=cursorobejct.fetchall()
    list_of_acc=[]
    for x in y:
        list_of_acc.append(x[0])
    
    
    for x in range(0,len(list_of_acc)):
        home_input=5
        if list_of_acc[x]==acc_no:
            cursorobejct.execute(f.CHECK__PASS,(acc_no,))
            q=cursorobejct.fetchall()
            my_value=q[0][0]
            
            if my_value==passw:
                home_input=client_home(acc_no)
                return home_input
            else:
                print('Enter  Valid Credentials\n\n\n\n')
            
            
            
            
        


#account generator#
def account_generator():
    num='1234567890'
    for x in range(0,1):
        passw=""
        for x in range(0,9):
            password_no=random.choice(num)
            passw=passw+password_no
        return passw


#email-phone number verification#


def check1(s,):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat,s):
        return 1
    else:
        return 0
    

#print balance_money#
def print_balance_money(facc):
    cursorobejct.execute(f.GET_CLIENT_ID,(facc,))
    q=cursorobejct.fetchall()
    value1=q[0][0]
    

    cursorobejct.execute(f.PRINT_CURRENT_BALANCE,(value1,))
    p=cursorobejct.fetchall()
    
    value2=p[0][0]

    return value2


#print bitcoin balance#
def print_bitcoin_money(facc):
    cursorobejct.execute(f.GET_CLIENT_ID,(facc,))
    q=cursorobejct.fetchall()
    value1=q[0][0]
    

    cursorobejct.execute(f.PRINT_CURRENT_BITCOIN_BALANCE,(value1,))
    p=cursorobejct.fetchall()
    
    value2=p[0][0]

    return value2

    
# money transfer and after transfer#
def money_transfer(facc,money,acc):
    cursorobejct.execute(f.GET_CLIENT_ID,(facc,))
    q=cursorobejct.fetchall()
    value1=q[0][0]

    cursorobejct.execute(f.PRINT_CURRENT_BALANCE,(value1,))
    p=cursorobejct.fetchall()
    value3=p[0][0]
    
    
    if money>value3:
        print("Insufficient Credit-------","\n\nCurrent balance= ",value3," .cr")
    else:
        
        value4=value3-money
       
        #query_values=(value4,value1)
        cursorobejct.execute(f.TRANSFER_MONEY,(value4,value1,))
        mydb.commit()

    


        cursorobejct.execute(f.GET_CLIENT_ID,(acc,))
        r=cursorobejct.fetchall()
        value5=r[0][0]

        cursorobejct.execute(f.PRINT_CURRENT_BALANCE,(value5,))
        s=cursorobejct.fetchall()
        value6=s[0][0]
        value7=value6+money
        
        cursorobejct.execute(f.TRANSFER_MONEY,(value7,value5,))
        mydb.commit()
        print("beneficiery money",value7)
        print("\n\n-----Money Transferred Sucessfully")

#email verification#

def verify_email(email):

    otp=random.randint(1000,9999)

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('studycourse683@gmail.com','ikbentjlzzkhsjza')
    msg='le rakh le apna otp ' +str(otp)

    server.sendmail('studycourse683@gmail.com',email,msg)
    otpu=int(input("Enter the otp send to your mail"))
    if otp==otpu:
        return 1
    else:
        return 0

    server.quit()


#password change email verification#

def password_change(facc,confirm_pass):
    cursorobejct.execute(f.GET_CLIENT_ID,(facc,))
    q=cursorobejct.fetchall()
    value1=q[0][0]

    cursorobejct.execute(f.GET_CLIENT_EMAIL,(value1,))
    r=cursorobejct.fetchall()
    value2=r[0][0]
    print(value2)

    p=verify_email(value2)
    
    if p==1:  
        
        cursorobejct.execute(f.GET_CLIENT_PASSWORD,(confirm_pass,value1,))
        mydb.commit()
        print("\n\nPassword changed successfull\n\n")
        
    else:
        print("Wrong otp Please try again")


#Bitcoin Transfer and after transfer#
def bitcoin_transfer(facc,bitcoin,acc):
    cursorobejct.execute(f.GET_CLIENT_ID,(facc,))
    q=cursorobejct.fetchall()
    value1=q[0][0]

    cursorobejct.execute(f.GET_BITCOIN_BALANCE,(value1,))
    p=cursorobejct.fetchall()
    value3=p[0][0]

    if bitcoin>value3:
         print("Insufficient Credit-------","\n\nCurrent balance= ",value3," ")
    else:
        value4=value3-bitcoin
       
        #query_values=(value4,value1)
        cursorobejct.execute(f.TRANSFER_BITCOIN,(value4,value1,))
        mydb.commit()

    


        cursorobejct.execute(f.GET_CLIENT_ID,(acc,))
        r=cursorobejct.fetchall()
        value5=r[0][0]

        cursorobejct.execute(f.GET_BITCOIN_BALANCE,(value5,))
        s=cursorobejct.fetchall()
        value6=s[0][0]
        value7=value6+bitcoin
        
        cursorobejct.execute(f.TRANSFER_BITCOIN,(value7,value5,))
        mydb.commit()
        print("beneficiery money",value7)
        print("\n\n-----Bitcoin Transferred Sucessfully")




        #MANAGER FUNCTION PLEASE NOT ALTER!#
        #MANAGER FUNCTION PLEASE NOT ALTER!#
        #MANAGER FUNCTION PLEASE NOT ALTER!#
        #MANAGER FUNCTION PLEASE NOT ALTER!#

def check_manager(username,passw):
    cursorobejct.execute(f.CHECK_ID_MANAGER,(username,))
    p=cursorobejct.fetchall()
    value1=p[0][0]
    if value1 is None:
        print("Wrong crdentials go away fake lord")
        return 0
    

    cursorobejct.execute(f.CHECK__PASS_MANAGER,(value1,))
    q=cursorobejct.fetchall()
    value2=q[0][0]

    if value2==passw:
        return 1
    else:
        print("you fake person do not dare to return back to this place")
        return 0


def manager_transaction(acc,mon):
    cursorobejct.execute(f.GET_CLIENT_ID,(acc,))
    p=cursorobejct.fetchall()
    value1=p[0][0]

    cursorobejct.execute(f.PRINT_CURRENT_BALANCE,(value1,))
    q=cursorobejct.fetchall()
    value3=q[0][0]

    value4=value3+mon

    cursorobejct.execute(f.TRANSFER_MONEY,(value4,value1,))
    mydb.commit()

    print("\n\nTransaction Success\n\n\n\n")



def countDigit(n):
                    count = 0
                    while n != 0:
                        n //= 10
                        count += 1
                    return count