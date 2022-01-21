from tkinter import *
def add():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    res = n1 + n2
    l3.configure(text="Sum is "+str(res))
def subtract():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    res = n1 - n2
    l3.configure(text="Difference is "+str(res))
def multiply():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    res = n1 * n2
    l3.configure(text="Product is "+str(res))
def divide():
    n1 = eval(t1.get())
    n2 = eval(t2.get())
    res = n1 / n2
    l3.configure(text="Quotient is "+str(res))
top = Tk()
top.geometry("400x300")
top.title("Calculator")
l1 = Label(top,text="Number 1")
l2 = Label(top,text="Number 2")
l1.place(x = 100, y = 50)
l2.place(x = 100, y = 80)
t1 = Entry(top, width = 10)
t2 = Entry(top, width = 10)
t1.place(x = 190, y = 50)
t2.place(x = 190, y = 80)
b1 = Button(top,text="+", command=add,font=("Arial Bold",30))
b2 = Button(top,text="-", command=subtract, font=("Arial Bold",30))
b3 = Button(top,text="*", command=multiply, font=("Arial Bold",30))
b4 = Button(top,text="/", command=divide, font=("Arial Bold",30))
b1.place(x = 100, y = 110)
b2.place(x = 190, y = 110)
b3.place(x = 100, y = 160)
b4.place(x = 190, y = 160)
l3 = Label(top,text="Result",font=("Arial",25))
l3.place(x = 120, y= 200)
top.mainloop()