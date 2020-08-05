from tkinter import *

prv = 0
znak = "0"

def kk1():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 1
    else:
        prv = 1

    chsl.insert(END, "1")
def kk2():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 2
    else:
        prv = 2
    chsl.insert(END, "2")
def kk3():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 3
    else:
        prv = 3
    chsl.insert(END, "3")
def kk4():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 4
    else:
        prv = 4
    chsl.insert(END, "4")
def kk5():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 5
    else:
        prv = 5
    chsl.insert(END, "5")
def kk6():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 6
    else:
        prv = 6
    chsl.insert(END, "6")
def kk7():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 7
    else:
        prv = 7
    chsl.insert(END, "7")
def kk8():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 8
    else:
        prv = 8
    chsl.insert(END, "8")
def kk9():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10 + 9
    else:
        prv = 9
    chsl.insert(END, "9")
def kk0():
    global pz
    global prv
    if prv != 0:
        prv = prv * 10
    chsl.insert(END, "0")
def znak1():
    global pz
    global prv
    global vtr
    global znak
    znak = 1
    vtr = prv
    prv = 0
    print(vtr)
    print("+")
    chsl.insert(END, " + ")

def znak2():
    global pz
    global prv
    global vtr
    global znak
    znak = 2
    vtr = prv
    prv = 0
    print(vtr)
    print("-")
    chsl.insert(END, " - ")

def znak3():
    global pz
    global prv
    global vtr
    global znak
    znak = 3
    vtr = prv
    prv = 0
    print(vtr)
    print("*")
    chsl.insert(END, " * ")

def znak4():
    global pz
    global prv
    global vtr
    global znak
    znak = 4
    vtr = prv
    prv = 0
    print(vtr)
    print("/")
    chsl.insert(END, " / ")




def rav():
    global otg
    global pz
    global prv
    global vtr
    global znak
    print(prv)
    print("=")
    if znak == 1:
        otg = prv + vtr
    elif znak == 2:
        otg = vtr - prv
    elif znak == 3:
        otg = prv * vtr
    elif znak == 4:
        otg = vtr / prv
    prv = 0
    print(otg)
    otg = " = " + str(otg)
    chsl.insert(END, otg)

def clr():
    global chsl
    global prv
    global vtr
    global otg
    chsl.delete(1.0, END)
    prv = 0
    vtr = 0
    otg = 0



kk = Tk(className='Kalkulator')
frame = Frame()
frame.pack()
kk.geometry("490x110")


chsl = Text(kk, height=1, width=30)
chsl.pack()

button1 = Button( text="1", fg="black", command=kk1)
button1.pack()
button1.place(x=30, y=54)

button2 = Button( text="2", fg="black", command=kk2)
button2.pack()
button2.place(x=50, y=54)

button3 = Button( text="3", fg="black", command=kk3)
button3.pack()
button3.place(x=70, y=54)

button4 = Button( text="4", fg="black", command=kk4)
button4.pack()
button4.place(x=30, y=27)

button5 = Button( text="5", fg="black", command=kk5)
button5.pack()
button5.place(x=50, y=27)

button6 = Button( text="6", fg="black", command=kk6)
button6.pack()
button6.place(x=70, y=27)

button7 = Button( text="7", fg="black", command=kk7)
button7.pack()
button7.place(x=30, y=0)

button8 = Button(text="8", fg="black", command=kk8)
button8.pack()
button8.place(x=50, y=0)

button9 = Button( text="9", fg="black", command=kk9)
button9.pack()
button9.place(x=70, y=0)

button0 = Button( text="0", fg="black", command=kk0)
button0.pack()
button0.place(x=30, y=81)

button_eq = Button( text="=", fg="black", command=rav)
button_eq.pack()
button_eq.place(x=68, y=81)

button_z1 = Button( text="+", fg="black", command=znak1)
button_z1.pack()
button_z1.place(x=95, y=0)

button_z2 = Button( text="-", fg="black", command=znak2)
button_z2.pack()
button_z2.place(x=95, y=27)

button_z3 = Button( text="*", fg="black", command=znak3)
button_z3.pack()
button_z3.place(x=95, y=54)

button_z4 = Button( text="/", fg="black", command=znak4)
button_z4.pack()
button_z4.place(x=95, y=81)

button_clr = Button( text="C", fg="black", command=clr)
button_clr.pack(side=BOTTOM)
button_clr.place()


kk.mainloop()
