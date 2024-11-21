from tkinter import *
from tkinter import messagebox
class third_page :
    def __init__(self , page):
        self.page = page
        self.page.resizable(0 , 0 )
        self.page.title("factorial page")
        self.page.geometry("500x600")
        self.page.config(bg="light blue")
        # entry
        self.number_entry = Entry(master=self.page, width=30)
        self.number_entry.place(x=190, y=220)
        # entry label
        self.num_lbl = Label(master=self.page, text=" عدد مورد نظر:", bg="light blue", fg="black", font=("MRT_Zohal 15"))
        self.num_lbl.place(x=80, y=212)
        # a label
        self.factorial_lbl = Label(master=self.page , text="محاسبه ی فاکتوریل ",font=("MRT_Zohal 50") , bg = "light blue")
        self.factorial_lbl.place(x=80 , y = 50)
        # a button
        btn = Button(master=page, text="click", width=18, height=4, bg="black", fg="white" , command=self.calc)
        btn.place(x=205, y=350)
        self.page.mainloop()
    def calc(self):
        try:
            num =int(self.number_entry.get())
            res = 1
            for item in range(2, num+1):
                res = res*item
            return messagebox.showinfo("result" ,f"فاکتوریل عدد مورد نظر شما:{res}")
        except:
            return  messagebox.showerror("error" , "لطفا یک عدد وارد کنید")



if __name__ == "__main__" :
    window =Tk()
    app = third_page(window)
    window.mainloop()