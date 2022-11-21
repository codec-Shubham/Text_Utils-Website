from tkinter import *
root = Tk()
root.geometry("400x600+500+100")
root.title("Calculator")
# root.overrideredirect(1)
root.wm_iconbitmap("calculator.ico")

scvalue = StringVar()
scvalue.set("")

def click(event):
   # global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
       if scvalue.get().isdigit():
           value = int(scvalue.get())
       else:
           try:
               value = eval(screen.get())
           except Exception as e:
               print(e)
               value = "Error"
       scvalue.set(value)
       screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
       scvalue.set(scvalue.get() + text )
       screen.update()

screen = Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f = Frame(root,bg="grey")
b = Button(f,text="9",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="8",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="7",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="6",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="5",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="4",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="3",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="2",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="1",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="0",padx=29,pady=20,font ="lucida 15 bold")
b.pack(side=LEFT,padx=7)
b.bind("<Button-1>",click)
b = Button(f,text="-",padx=28,pady=20,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="*",padx=30,pady=20,font ="lucida 15 bold")
b.pack(side=LEFT,padx=9)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="/",padx=29,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="%",padx=25,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=9)
b.bind("<Button-1>",click)
b = Button(f,text="=",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=7)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="c",padx=27,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text="+",padx=28,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
b = Button(f,text=".",padx=30,pady=22,font ="lucida 15 bold")
b.pack(side=LEFT,padx=8)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()