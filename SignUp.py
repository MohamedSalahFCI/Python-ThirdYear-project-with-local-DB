from tkinter import *
from tkinter import messagebox as m
from LoginForm import *

def SignUp(root,username,password,address,phonenum,age):
    if(username==""):
        m.showinfo("Error","You Must Enter all Information")
    elif(password==""):
        m.showinfo("Error", "You Must Enter all Information")
    elif (address == ""):
        m.showinfo("Error", "You Must Enter all Information")
    elif (phonenum == ""):
        m.showinfo("Error", "You Must Enter all Information")
    elif (age == ""):
        m.showinfo("Error", "You Must Enter all Information")
    else:
        lineinfile=username+";"+password+";"+address+";"+phonenum+";"+age+";"
        U=open("UserData.txt","a")
        U.write('\n'+lineinfile)
        U.close()
        loginFramForm=login_window2()
        loginFramForm.displaywin2(root,username)
class signupWindow:
    def __init__(self):
        root=Tk()
        root.title("SIgn Up Window")
        username=Label(root,text="User Name:-").grid(row=0,column=0)
        password = Label(root, text="Password:-").grid(row=1, column=0)
        Address = Label(root, text="Address:-").grid(row=2, column=0)
        phonenum = Label(root, text="phone Number:-").grid(row=3, column=0)
        Age = Label(root, text="Yor Age:-").grid(row=4, column=0)
        self.username=StringVar(master=root)
        username=Entry(root,textvariable=self.username).grid(row=0,column=1)
        self.password = StringVar(master=root)
        password= Entry(root,show="*",textvariable=self.password).grid(row=1, column=1)
        self.Address = StringVar(master=root)
        Address=Entry(root,textvariable=self.Address).grid(row=2, column=1)
        self.phonenum =StringVar(master=root)
        phonenum=Entry(root,textvariable=self.phonenum).grid(row=3, column=1)
        self.Age = StringVar(master=root)
        Age=Entry(root,textvariable=self.Age).grid(row=4, column=1)

        k=login_window2()
        signupButton=Button(root,text="Sign Up",command=lambda :SignUp(root,self.username.get(),self.password.get(),self.Address.get(),self.phonenum.get(),self.Age.get())).grid(row=8,column=0)
        haveAcc=Button(root,text="I Have Account",command=lambda :k.displaywin2(root,self.username)).grid(row=8,column=1)






        root.mainloop()

l=signupWindow()