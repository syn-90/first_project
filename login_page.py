from tkinter import *
import third_page
import register_page
import hashlib
import study
from tkinter import messagebox
import sql
class login :
    def __init__(self , page):
        self.page = page
        self.page.resizable(0 , 0 )
        self.page.title("login page")
        self.page.geometry("500x600")
        self.page.config(bg = "light blue")
        # name
        self.entry_name = Entry(master=self.page , width=50 )
        self.entry_name.place(x=120 , y = 100)
        self.lbl_name = Label(master=self.page , text= "نام :" , font=("MRT_Zohal 30") , bg = "light blue" )
        self.lbl_name.place(x =65 , y = 80 )
        # last name
        self.entry_lname = Entry(master=self.page , width=50 )
        self.entry_lname.place(x=120 , y = 230)
        self.lbl_lname = Label(master=self.page , text= "نام خانوادگی :" , font=("MRT_Zohal 20") , bg = "light blue" )
        self.lbl_lname.place(x =10 , y = 220 )
        # password
        self.entry_password = Entry(master=self.page , width=50 )
        self.entry_password.place(x=120 , y = 380)
        self.lbl_password = Label(master=self.page , text= " رمز عبور:" , font=("MRT_Zohal 25") , bg = "light blue" )
        self.lbl_password.place(x =10 , y = 355 )
        # login button
        self.btn = Button(master=self.page , text="ورود ", font=("MRT_Zohal 30") , width=10 , height=1 , command=self.check_from_db)
        self.btn.place(x=150 , y = 450)
        self.page.mainloop()
    def check_from_db(self):

        username =self.entry_name.get()
        lastname = self.entry_lname.get()
        password = self.entry_password.get()
        # hash password
        password2 = password.encode()
        h = hashlib.sha256()
        h.update(password2)
        hash_password = h.hexdigest()
        # check of username , lastname and password
        if username.replace(" ", "") != "" and lastname.replace(" ", "") != "" and password.replace(" ", "") != "":
            user =sql.sqlite(username,lastname,hash_password)
            res = user.select()
            if res != None:
                messagebox.showinfo("ok" , "خوش امدید")
                # leave this page
                self.page.destroy()
                window = Tk()
                app = third_page.third_page(page=window)
                return app
            elif res == None:
                messagebox.showerror("error" , "کاربری یافت نشد . لطفا ابتدا ثبت نام کنید")
                # going to register page
                self.page.destroy()
                root =  Tk()
                app = register_page.register(root)
                app

        else:
            messagebox.showerror("error", "لطفا نام و نام و خانوادگی و رمز عبور را وارد کنید")