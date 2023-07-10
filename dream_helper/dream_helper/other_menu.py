from tkinter import *
def color_resistor():
    pass

def paral_resistor():
    pass

def nominal_resistor():
    pass

def exit_but():
    tko.destroy()

def main():
    global tko
    tko = Tk()
    tko.geometry("500x500+550+150")
    tko.title("Персональний помічник. Додаткові можливості")
    tko.config(background="white")
    tit_other = Label(tko, text="Додаткові можливості", bg="white", font='Arial 20', foreground="black")
    but_other_1 = Button(tko, text="Визначення номіналу резистора за кольором", command=color_resistor, font="Arial 15", width=40)
    but_other_2 = Button(tko, text="Розрахунок паралельних з'єднань резисторів", command=paral_resistor, font="Arial 15", width=40)
    but_other_3 = Button(tko, text="Розрахунок номіналу резистора", command=nominal_resistor, font="Arial 15", width=40)
    but_exit = Button(tko, text="Вихід", command=exit_but, font="Arial 15", width=40)
    footer_other = Label(tko, text="© Dream Team", bg="white", font='Arial 10', foreground="black")
    tit_other.place(x=120, y=50)
    but_other_1.place(x=25, y=150)
    but_other_2.place(x=25, y=200)
    but_other_3.place(x=25, y=250)
    but_exit.place(x=25, y=300)
    footer_other.place(x=20, y=475)
    tko.mainloop()


if __name__ == '__main__':
    main()
