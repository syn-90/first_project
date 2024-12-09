from tkinter import *
import third_page
from tkinter import messagebox
import sql
import hashlib
import study
class register :
    def __init__(self , page):
        self.page = page
        self.page.resizable(0 , 0 )
        self.page.title("register page")
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
        # register button
        self.btn = Button(master=self.page , text="ثبت نام", font=("MRT_Zohal 30") , width=10 , height=1 , command=self.yas_or_no)
        self.btn.place(x=150 , y = 450)
        self.page.mainloop()
    # massege register
    def yas_or_no(self):
        yes_or_no = messagebox.askyesno("آیا تصمیم به ثبت نام دارید؟")
        if yes_or_no ==False:
            pass
        if yes_or_no==True:
            username = self.entry_name.get()
            lastname = self.entry_lname.get()
            password = self.entry_password.get()
            # hash password
            password2 = password.encode()
            h =hashlib.sha256()
            h.update(password2)
            hash_password =h.hexdigest()
            # checking of username , lastname and password
            if username.replace(" " , "") != "" and lastname.replace(" " , "") != "" and password.replace(" " , "") != "":
                # if this user is in database dont select that again
                user = study.sqlite(username, lastname, hash_password)
                res = user.select()
                if res != None:
                    messagebox.showinfo("register" , "شما قبلا ثبت نام کردید")
                if res == None:
                    user.insert()
                    messagebox.showinfo(title="yes", message="ثبت نام شما با موفقیت انجام شد")
                # log in to third page
                self.page.destroy()
                window = Tk()
                app = third_page.third_page(page=window)
                return app
            else:
                messagebox.showerror("error" , "لطفا نام و نام و خانوادگی و رمز عبور را وارد کنید")



if __name__ == "__main__" :
    window =Tk()
    app = register(window)
    window.mainloop()






