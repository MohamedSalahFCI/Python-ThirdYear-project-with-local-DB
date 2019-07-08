
from tkinter import *
from tkinter import messagebox as m
from WelcomPage import *

def displayMsg2():
    m.showinfo("User Status", "Invalide user name or password please try again  ")
class login_window2:

    def displaywin2(self,prewin,username):
        prewin.destroy()
        self.root=Tk()
        self.root.title("Sign In Window")
        usernamelabel=Label(self.root,text="User Name: ")
        usernamelabel.pack(anchor=NW)
        self.username=StringVar(master=self.root)
        self.password=StringVar(master=self.root)
        self.usernameEntry=Entry(self.root,bd=2,textvariable=self.username)
        self.usernameEntry.pack(anchor=NW)
        self.usernameEntry.focus()
        passwordlabel=Label(self.root,text="Password: ")
        passwordlabel.pack(anchor=NW)
        self.passwordEntry=Entry(self.root,textvariable=self.password,show="*")
        self.passwordEntry.pack(anchor=NW)
        c=login_window2()
        b=Button(self.root,text="Sign in",command=lambda :c.checkuser(self.root,self.username.get(),self.password.get(),self.passwordEntry,self.usernameEntry,self.username,self.password))
        b.pack()
        self.root.mainloop()

    def checkuser(self,root,username,password,usernameEntry,pwdEntry,userVar,pwdVar):
        u=[]
        pw=[]
        if(username == "") and (password == ""):
            pwdEntry.configure(background='red')
            usernameEntry.configure(background='red')
            userVar.set("")
            pwdVar.set("")
            usernameEntry.focus()
        elif (username == ""):
            usernameEntry.configure(background='red')
            userVar.set("")
            pwdVar  .set("")
            usernameEntry.focus()

        elif(password == ""):
            pwdEntry.configure(background='red')
            userVar.set("")
            pwdVar.set("")
            pwdEntry.focus()



        p=open("UserData.txt","r")
        for line in p:


            try:
                (usname,passw)=line.split(';',1)
                pwd=passw.split(';',1)
                u.append(usname)
                n=pwd[0].strip()
                pw.append(n)

            except ValueError:
                pass
        i=0
        flag=0
        while(i<len(u)):
            if username==u[i] and  password==pw[i]:
                flag=1
                s=sayHi()
                break
            else:

                i=i+1

        if flag==0:
            m.showwarning("Status","Invalid user name and password")




        p.close()



login=login_window2()

