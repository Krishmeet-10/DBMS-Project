from tkinter import *

from regex import P
root=Tk()

root.title("OLA Cabs")
root.geometry("800x720")

root.resizable(False,False)

Label(root,text=" OLA Cabs User [Login/Signup]",font=25).pack(pady=45)

Label(text="Name",font=25).place(x=150,y=175)
Label(text="Phone Number",font=25).place(x=150,y=300)
Label(text="Email",font=25).place(x=150,y=425)

name=StringVar()
ph_no = int()
email = StringVar()

name_entry=Entry(root,textvariable=name,width=35,bd=3,font=25)
name_entry.place(x=225,y=175)

pno_entry=Entry(root,textvariable=ph_no,width=30,bd=3,font=25)
pno_entry.place(x=300,y=300)

email_entry=Entry(root,textvariable=email,width=30,bd=3,font=25)
email_entry.place(x=250,y=425)

def register():
    a=name_entry.get()
    b=pno_entry.get()
    c=email_entry.get()
    print(a+" "+b+" "+c)

    print("User Entered in Database")
    

Button(text="login/Register",font=25,width=11,height=2,command=register).place(x=300,y=550)

root.mainloop()


