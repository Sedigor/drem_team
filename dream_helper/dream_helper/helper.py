from tkinter import *
import addressbook
import notebook
import sort
import other

def addressbook_but():
    addressbook.main()

def notebook_but():
    notebook.main()

def sorter_but():
    sort.main()

def other_but():
    other.main()

def exit_but():
    tk.destroy()
    try:
        addressbook.tka.destroy()
        notebook.tkn.destroy()
        sort.tks.destroy()
    except:
        print("Goodbye!")


def main():
    global tk
    tk = Tk()
    tk.geometry("500x500+430+50")
    tk.title("Персональний помічник")
    tk.config(background="grey")
    tit = Label(tk, text="Персональний помічник вітає Вас!", bg="grey", font='Arial 20', foreground="white")
    but_1 = Button(tk, text="Адресна книга", command=addressbook_but, font="Arial 15", width=18)
    but_2 = Button(tk, text="Нотатник", command=notebook_but, font="Arial 15", width=18)
    but_3 = Button(tk, text="Сортувальник", command=sorter_but, font="Arial 15", width=18)
    but_4 = Button(tk, text="Інше", command=other_but, font="Arial 15", width=18)
    but_5 = Button(tk, text="Вихід", command=exit_but, font="Arial 15", width=18)
    footer = Label(tk, text="© Dream Team", bg="grey", font='Arial 10', foreground="white")
    tit.place(x=30, y=50)
    but_1.place(x=150, y=150)
    but_2.place(x=150, y=200)
    but_3.place(x=150, y=250)
    but_4.place(x=150, y=300)
    but_5.place(x=150, y=350)
    footer.place(x=20, y=475)
    tk.mainloop()



if __name__ == '__main__':
    main()
