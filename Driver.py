from tkinter import *

from regex import P
root=Tk()

root.title("OLA Cabs")
root.geometry("800x720")

root.resizable(False,False)

Label(root,text=" OLA Cabs Driver Portal [Login/Signup]",font=25).pack(pady=45)

Label(text="Name",font=25).place(x=150,y=175)
Label(text="Phone Number",font=25).place(x=150,y=300)
Label(text="Bank Details",font=25).place(x=150,y=425)

name=StringVar()
ph_no = int()
bank = StringVar()

name_entry=Entry(root,textvariable=name,width=35,bd=3,font=25)
name_entry.place(x=225,y=175)

pno_entry=Entry(root,textvariable=ph_no,width=30,bd=3,font=25)
pno_entry.place(x=300,y=300)

bank_entry=Entry(root,textvariable=bank,width=30,bd=3,font=25)
bank_entry.place(x=300,y=425)

def register():
    a=name_entry.get()
    b=pno_entry.get()
    c=bank_entry.get()
    #print(type(int(c)))
    print(a+" "+b+" "+c)

    print("User Entered in Database")
    

Button(text="login/Register",font=25,width=11,height=2,command=register).place(x=300,y=550)

root.mainloop()


