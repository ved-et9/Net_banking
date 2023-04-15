import data as d
import functions as f
import os

MENU="""--------------NET BANKING----------------\t\t\t\t\t\t\t\t\t\t\t#)ADMIN LOG IN

Please Choose one of these options:

1)Sign up

2)Log in



Your Selection:  """

def menu ():
    
    while(user_input:=input(MENU))!="3":
        os.system('cls')
        if user_input=="1":
            adhaar=int(input("ENTER YOUR adhaar_no.: "))
            s=d.check(adhaar)
            if s!="1":
                fname=input("ENTER YOUR FIRST NAME: ").capitalize()
                lname=input("ENTER YOUR LAST NAME: ").capitalize()
                email=input("ENTER YOUR Valid Email id: ").capitalize()
                mobile_no=int(input("ENTER YOUR Mobile no.: "))
                #tm=d.countDigit(mobile_no)
                #if tm!=10:
                    #print("enetr valid mobile no")
                adhaar=int(input("ENTER YOUR adhaar_no.: "))
               
                #te=d.countDigit(adhaar)
                #if tm!=10:
                  #  print("enetr valid adhaar")
                otp=d.verify_email(email)
                if otp!=1:
                    print("invalid otp")
                    break
                
                account_no=d.account_generator()

                
                passw=input("ENTER YOUR New Password: ")
                q=d.check1(email,)
                if q==1:
                    d.new_login(adhaar,account_no,passw,fname,lname,email,mobile_no)
                    print("""--------------WELCOME TO HP FAMILY-----------\n\n\n
                    Your Account created successfully""")
                    print("Name= ",fname,"",lname,"\nAdhaar No.= ",adhaar,"\nEmail= ",email,"\nMobile no.= ",mobile_no,"\nAccount No.= ",account_no)
                    print("\n\n\n\nPLEASE REMEMBER YOUR ACCOUNT NUMBER AND PASSWORD FOR FURTHER USE")
                else:
                    print("Invalid input by user")
                
        elif user_input=="2":
            print("WELCOME TO HP BANK\n\n")
            facc=int(input("Enter Your account_no. : "))
            fpass=input("Enter the password:")
            home_input=d.user(facc,fpass)
            if home_input==1:
                
                money=d.print_balance_money(facc)
                print("YOur current Balance is: ",money)

            elif home_input==2:
                
                bitcoin=d.print_bitcoin_money(facc)
                print("\n\nYour Current BITCOIN Wallte Balance is: ",bitcoin,"\n\n\n")

            elif home_input==3:
                t=int(input(f.SUB_TRANSFER))
                if t==1:
                    print("Transfer money:\n\n")
                    acc=int(input("Enter the Beneficiery Account no."))
                    money_transfer=int(input("\nEnter the amount of money to be transfered: "))
                    d.money_transfer(facc,money_transfer,acc)
                if t==2:
                    print("---------------\nTransfer Bitcoin\n\n")
                    acc=int(input("Enter the Beneficiery Account no."))
                    bitcoin=int(input("Enter the amount of bitcoin to be transfered: "))
                    d.bitcoin_transfer(facc,bitcoin,acc)

            elif home_input==4:
                new_pass=input("Enter New Password")
                confirm_pass=input("Confirm Your Password")
                if new_pass==confirm_pass:
                    d.password_change(facc,confirm_pass)
                else:
                    print("Password do not match")

                

            else:
                continue


        elif user_input=='#':
            print("WELCOME LORD    The only light The world Can Have Right Now")
            x=input(f.I)
            y=input(f.J)
            ans=d.check_manager(x,y)
            if ans==1:
                print("Lord Welcome")
                z=int(input(f.LORD_MENU))
                if z==1:
                    acc=int(input("Enter the customer account no.  \n\n"))
                    mon=int(input("Enter the amount of money: "))
                    d.manager_transaction(acc,mon)
                    

        else:
            print("Invalid Input")

menu()