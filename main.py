from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Shreya1201!", database="python")
print(mydb)
if (mydb):
    print("successful")
else:
    print("no")
mycursor=mydb.cursor()

def DropPlace(ride_id):
    sql2 = f"select destination from ride_details where ride_id='{ride_id}'"
    mycursor.execute(sql2)
    dest=mycursor.fetchall()

    return dest[0][0]

def Pick(ride_id):
    sql2 = f"select pick from ride_details where ride_id='{ride_id}'"
    mycursor.execute(sql2)
    pi=mycursor.fetchall()

    return pi[0][0]

def amount(ride_id):
    sql2 = f"select amouunt from ride_details where ride_id='{ride_id}'"
    mycursor.execute(sql2)
    amt=mycursor.fetchall()

    return amt[0][0]

def dPhone(ride_id):
    sql2 = f"select driver_phone from ride_details where ride_id='{ride_id}'"
    mycursor.execute(sql2)
    phone=mycursor.fetchall()

    return phone[0][0]
# def fixOutput(givenString):
#     new_str=''
#     for char in givenString:
#         if char!='(' and char!=')' and char!='[' and char!=']':
#             new_str+=char
#             return new_str

window=Tk()
Frame_details=Frame(window,bg="white")
Frame_details.place(x=0,y=0,height=800,width=500)
l1=Label(Frame_details, text="         Ride Details",font=("Arial",30,"bold")).place(x=90,y=80)

ride_id=4522

desc=Label(Frame_details, text=f"          Your cab with number {ride_id} is on its way ",font=("Times New Roman",15)).place(x=90,y=125)

# adding map image
# img = ImageTk.PhotoImage(Image.open("map.jpeg"))
# imgLabel = Label(Frame_details, image = img)
# imgLabel.pack()

pLoc=Button(Frame_details, text=f"       Pick up location: {Pick(ride_id)}   ",font=("Times New Roman",18)).place(x=97,y=360)
dLoc=Button(Frame_details, text=f"    Drop location: {DropPlace(ride_id)}     ",font=("Times New Roman",18)).place(x=105,y=400)

dPhone=Button(Frame_details, text=f"      Call driver at {dPhone(ride_id)}  ",cursor="hand1",bg="white",font=("Times New Roman",15,"bold")).place(x=160,y=450)
paymentAmount=Label(Frame_details, text=f"                      Please pay: {amount(ride_id)}",font=("Times New Roman",15,"bold")).place(x=130,y=480)
payment=Label(Frame_details, text="              Payment method: Cash",font=("Times New Roman",15,"bold")).place(x=136,y=500)


window.mainloop()
