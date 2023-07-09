from tkinter import *
def find_notes():
    pass

def add_note():
    pass

def change_note():
    pass

def del_note():
    pass

def exit_but():
    tkn.destroy()

def main():
    global tkn
    tkn = Tk()
    tkn.geometry("500x500+550+150")
    tkn.title("Персональний помічник. Нотатник")
    tkn.config(background="white")
    tit_nb = Label(tkn, text="Нотатки", bg="white", font='Arial 20', foreground="black")
    but_nb_1 = Button(tkn, text="Знайти нотатки", command=find_notes, font="Arial 15", width=18)
    but_nb_2 = Button(tkn, text="Додати запис", command=add_note, font="Arial 15", width=18)
    but_nb_3 = Button(tkn, text="Змінити запис", command=change_note, font="Arial 15", width=18)
    but_nb_4 = Button(tkn, text="Видалити запис", command=del_note, font="Arial 15", width=18)
    but_nb_5 = Button(tkn, text="Вихід", command=exit_but, font="Arial 15", width=18)
    footer_nb = Label(tkn, text="© Dream Team", bg="white", font='Arial 10', foreground="black")
    tit_nb.place(x=200, y=50)
    but_nb_1.place(x=150, y=150)
    but_nb_2.place(x=150, y=200)
    but_nb_3.place(x=150, y=250)
    but_nb_4.place(x=150, y=300)
    but_nb_5.place(x=150, y=350)
    footer_nb.place(x=20, y=475)
    tkn.mainloop()


if __name__ == '__main__':
    main()
