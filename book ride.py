import mysql.connector
from tkinter import *
from tkinter import messagebox
import random
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password = 'Sejwal@123',
#     port = '3306',
#     database = 'new_ola'
# )
#
# cursor = mydb.cursor()
# cursor.execute('SELECT * FROM car')
# users = cursor.fetchall()
# for i in users:
#     print(i)


def Ok():
    phone = e1.get()
    pick = e2.get()
    dest = e3.get()
    cash = e4.get()
    card = e5.get()
    if card == "":
        card = 0
    upi = e6.get()




    mysqldb=mysql.connector.connect(
        host='localhost',
        user='root',
        password = 'Sejwal@123',
        port = '3306',
        database = 'new_ola'
    )
    mycursor=mysqldb.cursor()

    try:
#         INSERT INTO `new_ola`.`car`
# (`id`,
#  `name`,
#  `pass`)
# VALUES
# (<{id: }>,
#  <{name: }>,
#  <{pass: }>);

        # d_phone
        mycursor.execute('SELECT * FROM new_ola.drivers order by rand() limit 1')
        driver = mycursor.fetchall()
        d_phone = driver[0][0]
        amount = random.randint(200, 3500)
        print(amount)

        # sql = "INSERT INTO car (id,name,pass) VALUES (%d, %s, %s)"
        sql = f"INSERT INTO new_ola.ride_details value({d_phone},{phone},'{pick}','{dest}',{amount},0,'{cash}',{card},'{upi}')"
        # # val = (id,name,passw)
        mycursor.execute(sql)
        mysqldb.commit()
        messagebox.showinfo("information", "Record inserted successfully...")


    except Exception as e:

        print(e)
        # print("err")
        mysqldb.rollback()
        mysqldb.close()

root = Tk()
root.title("Book a Ride")
root.geometry("300x300")
global e1
global e2
global e3
global e4
global e5
global e6

Label(root, text="user phone").place(x=10, y=10)
Label(root, text="pickup").place(x=10, y=40)
Label(root, text="destination").place(x=10, y=80)
Label(root, text="cash (yes/no)").place(x=10, y=120)
Label(root, text="Card details (O)").place(x=10, y=160)
Label(root, text="UPI reference (O)").place(x=10, y=200)


e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=80)

e4 = Entry(root)
e4.place(x=140, y=120)

e5 = Entry(root)
e5.place(x=140, y=160)

e6 = Entry(root)
e6.place(x=140, y=200)

Button(root, text="Add", command=Ok ,height = 3, width = 13).place(x=10, y=230)


root.mainloop()



