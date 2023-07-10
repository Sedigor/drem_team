from tkinter import *

def but_find():
    print(c1.get(), c2.get(), c3.get(), c4.get(), c5.get())

def but_exit():
    tkf.destroy()


def main():
    global tkf, c1, c2, c3, c4, c5
    tkf = Tk()
    tkf.geometry("300x350+550+150")
    tkf.title("Пошук в адресній книзі")
    lab = Label(tkf, text="Пошук за:", font='Arial 20')
    c1 = BooleanVar()
    c2 = BooleanVar()
    c3 = BooleanVar()
    c4 = BooleanVar()
    c5 = BooleanVar()
    chk1 = Checkbutton(tkf, text="ім'ям", font="Arial 15", variable=c1)
    chk2 = Checkbutton(tkf, text="телефоном", font="Arial 15", variable=c2)
    chk3 = Checkbutton(tkf, text="електронною поштою",
                       font="Arial 15", variable=c3)
    chk4 = Checkbutton(tkf, text="адресою", font="Arial 15", variable=c4)
    chk5 = Checkbutton(tkf, text="примітками", font="Arial 15", variable=c5)
    but_f = Button(tkf, text="Шукати", font="Arial 15",
                   width=8, command=but_find)
    but_ex = Button(tkf, text="Вихід", font="Arial 15", width=8, command=but_exit)
    lab.pack()
    chk1.place(x=30, y=50)
    chk2.place(x=30, y=100)
    chk3.place(x=30, y=150)
    chk4.place(x=30, y=200)
    chk5.place(x=30, y=250)
    but_f.place(x=30, y=300)
    but_ex.place(x=170, y=300)
    tkf.mainloop()


if __name__ == '__main__':
    main()
