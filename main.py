
import mysql.connector
import datetime    
import os 

#print((datetime.date.today()))
mydate=str(datetime.date.today())
today=mydate[8:10]+mydate[5:7]
myconnection=mysql.connector.connect( host="localhost", user="root", password="mysql", database="bday")
curr=myconnection.cursor()
curr.execute(f"select *from dates where bday = {today}")
li=curr.fetchall()

for i in li:
    print(i)

for i in li:
    os.system(f"start https://web.whatsapp.com/send?phone=+91{i[2]}^&text=Wishing%20You%20Happy%20Birthday%20Have%20a%20Bash%20{i[0]}")
