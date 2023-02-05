import random
import smtplib

otp=random.randint(1000,9999)

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('studycourse683@gmail.com','ikbentjlzzkhsjza')
msg='le rakh le apna otp ' +str(otp)

server.sendmail('studycourse683@gmail.com','singhvedu979@gmail.com',msg)
server.quit()