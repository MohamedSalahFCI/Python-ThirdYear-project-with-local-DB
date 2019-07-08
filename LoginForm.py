from tkinter import *
from tkinter import messagebox as m
from WelcomPage import *

def displayMsg2():
    m.showinfo("User Status", "Invalide user name or password please try again  ")
class login_window2:




    def displaywin2(self,prewin,username):
        #3shan l gui aly 2apleha ya5tafy
        prewin.destroy()
        root=Tk()
        root.title("Sign In Window")
        usernamelabel=Label(root,text="User Name: ").grid(row=0,column=0)
        passwordlabel = Label(root, text="password: ").grid(row=1, column=0)
        self.username=StringVar(master=root)
        self.password = StringVar(master=root)
        self.usernameEntry=Entry(root,textvariable=self.username).grid(row=0,column=1)
        self.passwordEntry=Entry(root,textvariable=self.password).grid(row=1,column=1)

        c=login_window2()
        loginButton=Button(root,text="Sign in",command=lambda :c.Usercheck(root,self.username.get(),self.password.get(),self.usernameEntry,self.passwordEntry)).grid(row=2,column=0)
        root.mainloop()


    def Usercheck(self,root,username,password,usernameEntry,passwordEntry):
        m.showinfo("message","soacpap")
        welcome=sayHi()
        user=[]
        userpass=[]

        if(username=="") and (password==""):
            m.showinfo("message", "usandpas")
           # passwordEntry.configure(background='red')
            #usernameEntry.configure(background='red')
           # userVar.set("")
            #passVariable.set("")
        elif(username==""):
            m.showinfo("message", "us")
           # usernameEntry.configure(background='red')
            #userVar.set("")
            #passVariable.set("")
            #usernameEntry.focus()
        elif(password==""):
            m.showinfo("message", "pass")
           # passwordEntry.configure(background='red')
            #userVar.set("")
            #passVariable.set("")
            #passwordEntry.focus()

        else:

            p = open("UserData.txt", "r")
            for line in p:
                try:
                    (formUserName, fullString) = line.split(';', 1)
                    formPasswordwithsomechar = fullString.split(';', 1)
                    user.append(formUserName)
                    n = formPasswordwithsomechar[0].strip()
                    userpass.append(n)
                except ValueError:
                    pass

            i=0
            flag=0
            while(i<len(user)):
                if username==user[i] and password==userpass[i]:
                    print("_f_" + username + "__")
                    print("_g_" + user[i] + "__")
                    flag=1
                    welcome.sayhi(root)
                    break
                else:
                    print("_k_" + username + "__")
                    print("_l_" + user[i] + "__")
                    i=i+1
            if flag==0:
                m.showwarning("Status","Invalid username and password")


            p.close()



l=login_window2()