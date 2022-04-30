from tkinter import *

from regex import P
root=Tk()

root.title("OLA Cabs")
root.geometry("800x720")

root.resizable(False,False)

Label(root,text="Car Details",font=25).pack(pady=45)

Label(text="Model",font=25).place(x=150,y=175)
Label(text="Capacity",font=25).place(x=150,y=300)
Label(text="Registration Date",font=25).place(x=150,y=425)

model=StringVar()
capacity = int()
reg = StringVar()

model_entry=Entry(root,textvariable=model,width=35,bd=3,font=25)
model_entry.place(x=225,y=175)

pno_entry=Entry(root,textvariable=capacity,width=30,bd=3,font=25)
pno_entry.place(x=250,y=300)

reg_entry=Entry(root,textvariable=reg,width=30,bd=3,font=25)
reg_entry.place(x=350,y=425)

def register():
    a=model_entry.get()
    b=pno_entry.get()
    c=reg_entry.get()
    #print(type(int(c)))
    print(a+" "+b+" "+c)

    print("User Entered in Database")
    

Button(text="login/Register",font=25,width=11,height=2,command=register).place(x=300,y=550)

root.mainloop()


