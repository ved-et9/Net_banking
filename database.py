from asyncio import create_subprocess_exec
import os
import psycopg2

mydb = psycopg2.connect(os.environ["DATABASE_URL"])

with mydb.cursor() as cursorobject:

    qry="""CREATE TABLE client_info (
    client_id BIGINT NOT NULL PRIMARY KEY,
    account_no INT NOT NULL,
    passw VARCHAR NOT NULL,
    first_name CHAR NOT NULL,
    last_name CHAR NOT NULL,
    email VARCHAR NOT NULL,
    mobile_no BIGINT NOT NULL)"""
    qry_2="""INSERT INTO client_info (client_id,account_no,passw,first_name,last_name,email,mobile_no)
     VALUES ('162838292928','345262628281','ABC#@12','V','S','singhvedu979@gmail.com','9301726352');"""
   
    cursorobject.execute(qry_2)
    mydb.commit()
    

