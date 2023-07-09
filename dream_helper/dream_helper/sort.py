from tkinter import *
def sorter():
    folder = ent_sort.get()
    if folder == "c":
        print("Ok")

def exit_but():
    tks.destroy()

def main():
    global tks, ent_sort
    tks = Tk()
    tks.geometry("500x250+350+100")
    tks.title("Персональний помічник. Сортувальник файлів")
    tks.config(background="black")
    tit_sort = Label(tks, text="Уведіть адресу папки для сортування", bg="black", font='Arial 20', foreground="white")
    ent_sort = Entry(tks, font="Arial 15")
    but_sort_1 = Button(tks, text="Сортувати", command=sorter, font="Arial 15", width=15)
    but_sort_2 = Button(tks, text="Вихід", command=exit_but, font="Arial 15", width=15)
    footer_sort = Label(tks, text="© Dream Team", bg="black", font='Arial 10', foreground="white")
    tit_sort.place(x=5, y=20)
    ent_sort.place(x=50, y=80, width=400, height=50)
    but_sort_1.place(x=50, y=150)
    but_sort_2.place(x=280, y=150)
    footer_sort.place(x=20, y=225)
    tks.mainloop()


if __name__ == '__main__':
    main()
