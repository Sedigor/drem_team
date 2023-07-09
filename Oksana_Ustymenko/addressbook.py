from tkinter import *
def find_contacts():
    pass

def birthdays():
    pass

def add_contact():
    pass

def change_contact():
    pass

def del_contact():
    pass

def exit_but():
    tka.destroy()

def main():
    global tka
    tka = Tk()
    tka.geometry("500x500+500+100")
    tka.title("Персональний помічник. Адресна книга")
    tka.config(background="light grey")
    tit_ab = Label(tka, text="Адресна книга", bg="light grey", font='Arial 20', foreground="black")
    but_ab_1 = Button(tka, text="Знайти контакти", command=find_contacts, font="Arial 15", width=18)
    but_ab_2 = Button(tka, text="Дні народження", command=birthdays, font="Arial 15", width=18)
    but_ab_3 = Button(tka, text="Додати запис", command=add_contact, font="Arial 15", width=18)
    but_ab_4 = Button(tka, text="Змінити запис", command=change_contact, font="Arial 15", width=18)
    but_ab_5 = Button(tka, text="Видалити запис", command=del_contact, font="Arial 15", width=18)
    but_ab_6 = Button(tka, text="Вихід", command=exit_but, font="Arial 15", width=18)
    footer_ab = Label(tka, text="© Dream Team", bg="light grey", font='Arial 10', foreground="black")
    tit_ab.place(x=160, y=50)
    but_ab_1.place(x=150, y=150)
    but_ab_2.place(x=150, y=200)
    but_ab_3.place(x=150, y=250)
    but_ab_4.place(x=150, y=300)
    but_ab_5.place(x=150, y=350)
    but_ab_6.place(x=150, y=400)
    footer_ab.place(x=20, y=475)
    tka.mainloop()


if __name__ == '__main__':
    main()
