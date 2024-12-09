# this is first page
from tkinter import *
import register_page
import login_page
class first_page:
    def __init__(self , page):
        self.page = page
        self.page.resizable(0 , 0 )
        self.page.title("first page")
        self.page.geometry("500x600")
        self.page.config(bg = "light blue")
        # label
        self.page.lbl = Label(master=self.page , bg = "light blue" , text="به برنامه ی محاسبه ی فاکتوریل خوش آمدید" , font=("MRT_Zohal 25"))
        self.page.lbl.place(x=20 , y = 40)

        # button login
        self.login_button = Button(master=self.page , text= "ورود" , font="MRT_Zohal 30" , width=15, height=1 ,command=self.login_page)
        self.login_button.place(x=100 , y =300)

        # button register
        self.register_button = Button(master=self.page , text= "ثبت نام" , font="MRT_Zohal 30" , width=15 , height=1 ,command=self.register_page)
        self.register_button.place(x=100 , y =450)

# a function for register button
    def register_page(self):
        self.page.destroy()
        page = Tk()
        app= register_page.register(page=page)
        return app
# a function for login button
    def login_page(self):
        self.page.destroy()
        page = Tk()
        app= login_page.login(page=page)
        return app



if __name__ == "__main__" :
    window =Tk()
    app = first_page(window)
    window.mainloop()