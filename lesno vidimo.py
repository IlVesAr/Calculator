from tkinter import *
prv = 0
znak = "0"

def kka(num):
    global a
    global chsl
    global prv
    if prv != 0:
        prv = prv * 10 + num
    else:
        prv = num
    a = num
    chsl.insert(END, num)


def znaka(z):
    global prv
    global vtr
    global znak
    znak = z
    vtr = prv
    prv = 0
    print(vtr)
    print(znak)
    chsl.insert(END, znak)

def rav():
    global otg
    global prv
    global vtr
    global znak
    print(prv)
    print("=")
    try:
        if znak == " + ":
            otg = prv + vtr
        elif znak == " - ":
            otg = vtr - prv
        elif znak == " * ":
            otg = prv * vtr
        elif znak == " / ":
            otg = vtr / prv
        prv = 0
        print(otg)
        chsl.insert(END, " = ")
        chsl.insert(END, otg)
    except:
        chsl.insert(END, " = sori")
        print("sori")


def clr():
    global chsl
    global prv
    global vtr
    global otg
    chsl.delete(1.0, END)
    prv = 0
    vtr = 0
    otg = 0

kk = Tk()
frame = Frame()
frame.pack()
chsl = Text(kk, height=1, width=30)
chsl.pack()
kk.title("Kalkulator")
kk.geometry("490x110")

button1 = Button(kk, text="1", fg="black", command=lambda: kka(1))
button1.pack()
button1.place(x=30, y=54)

button2 = Button(kk, text="2", fg="black", command=lambda: kka(2))
button2.pack()
button2.place(x=50, y=54)

button3 = Button(text="3", fg="black", command=lambda: kka(3))
button3.pack()
button3.place(x=70, y=54)

button4 = Button(text="4", fg="black", command=lambda: kka(4))
button4.pack()
button4.place(x=30, y=27)

button5 = Button(text="5", fg="black", command=lambda: kka(5))
button5.pack()
button5.place(x=50, y=27)

button6 = Button(text="6", fg="black", command=lambda: kka(6))
button6.pack()
button6.place(x=70, y=27)

button7 = Button(text="7", fg="black", command=lambda: kka(7))
button7.pack()
button7.place(x=30, y=0)

button8 = Button(text="8", fg="black", command=lambda: kka(8))
button8.pack()
button8.place(x=50, y=0)

button9 = Button(text="9", fg="black", command=lambda: kka(9))
button9.pack()
button9.place(x=70, y=0)

button0 = Button(text="0", fg="black", command=lambda: kka(0))
button0.pack()
button0.place(x=30, y=81)

button_eq = Button(text="=", fg="black", command=rav)
button_eq.pack()
button_eq.place(x=68, y=81)

button_z1 = Button(text="+", fg="black", command=lambda: znaka(" + "))
button_z1.pack()
button_z1.place(x=95, y=0)

button_z2 = Button(text="-", fg="black", command=lambda: znaka(" - "))
button_z2.pack()
button_z2.place(x=95, y=27)

button_z3 = Button(text="*", fg="black", command=lambda: znaka(" * "))
button_z3.pack()
button_z3.place(x=95, y=54)

button_z4 = Button(text="/", fg="black", command=lambda: znaka(" / "))
button_z4.pack()
button_z4.place(x=95, y=81)

button_clr = Button( text="C", fg="black", command=clr)
button_clr.pack(side=BOTTOM)
button_clr.place()

kk.mainloop()