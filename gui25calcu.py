from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
               value=eval(screen.get()) 
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("550x400")
root.title("Calculator")
root.configure(bg="black")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font="lucida 40 bold",bg="orange")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f1 = Frame(root,bg="black")
b=Button(f1,text="9",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="8",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="7",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="6",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="5",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="*",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,bg="black")


b=Button(f1,text="4",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="3",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="2",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="1",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="0",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)


b=Button(f1,text="-",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

f1.pack()

f1 = Frame(root,bg="black")

b=Button(f1,text="C",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="/",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="+",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="%",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)


b=Button(f1,text=".",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

b=Button(f1,text="=",padx=16,pady=12,font="lucida 25 bold",bg="orange")
b.pack(side=LEFT,padx=8,pady=5)
b.bind("<Button-1>",click)

f1.pack()


root.mainloop()