from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("400x400")
# Label(win,text="login:").grid(column=0,row=0)
# Label(win,text="Pasword:").grid(column=0,row=1)
# Entry(win,width=20).grid(column=1,row=0,pady=5)
# Entry(win,width=20).grid(column=1,row=1,pady=5)
# Button(win,text="Autorisation").grid(column=1,row=2,sticky=E)


# from random import randint
# def move(e):
#     btn.place(x=randint(0,300),y=randint(0,300))
#
#
# btn = Button(win, text="Поймай меня",bg="pink")
# btn.place(x=10,y=10)
# btn.bind("<Enter>", move)


# from random import randint
# def switch():
#     rb_val.set(randint(1,5))
#     win.after(1000, switch)
#
# fr = Frame(win)
# fr.pack(anchor=NW)
#
# rb_val = IntVar()
# rb1 = Radiobutton(win,variable=rb_val,value=1)
# rb1.pack(side=LEFT)
# rb2 = Radiobutton(win,variable=rb_val,value=2)
# rb2.pack(side=LEFT)
# rb3 = Radiobutton(win,variable=rb_val,value=3)
# rb3.pack(side=LEFT)
# rb4 = Radiobutton(win,variable=rb_val,value=4)
# rb4.pack(side=LEFT)
# rb5 = Radiobutton(win,variable=rb_val,value=5)
# rb5.pack(side=LEFT)
#
# switch()

# def func1(bind_e):
#     indx1= lstbox1.curselection()[0]
#     pgrase[0] = lst1[indx1]
#     ent["state"] = "normal"
#     ent.delete(0, END)
#     ent.insert(0,f"{pgrase[0]} {pgrase[1]}")
#     ent["state"] = "readonly"
# def func2(bind_e):
#     indx2 = lstbox2.curselection()[0]
#     pgrase[1] = lst2[indx2]
#     ent["state"] = "normal"
#     ent.delete(0, END)
#     ent.insert(0, f"{pgrase[0]} {pgrase[1]}")
#     ent["state"] = "readonly"
#
#
# pgrase = ["", ""]
# lst1 = ["обоятельный", "нервный", "здравый", "опасный", "саблезубый", "заниженный", "адекватный"]
# lst2 = ["пакет", "доклад", "гость", "заезд", "поршень", "унитаз", "объект"]
# lst1_tk = StringVar(value=lst1)
# lst2_tk = StringVar(value=lst2)
#
# lstbox1 = Listbox(win, listvariable=lst1_tk)
# lstbox1.grid(column=0,row=0,pady=10,padx=10)
# lstbox1.bind('<<ListboxSelect>>',func1)
# lstbox2 = Listbox(win, listvariable=lst2_tk)
# lstbox2.grid(column=1,row=0,pady=10,padx=10)
# lstbox2.bind('<<ListboxSelect>>',func2)
# ent = Entry(win,width=30)
# ent.insert(0,"...")
# ent['state'] = "readonly"
# ent.grid(column=0,row=1,columnspan=2)


def hello():
    if gender.get() == 1:
        messagebox.showinfo("hge",f"mr{ent1.get()}")
    else:
        messagebox.showinfo("nrufib",f"ms{ent2.get()}")

ent1 = Entry(win)
ent1.grid(row=0,column=1)
ent2 = Entry(win,show="*")
ent2.grid(row=1,column=1)

gender = IntVar()
fr = LabelFrame(win,text="Gender")
fr.grid(row=2,column=0,columnspan=2)
rb1 = Radiobutton(fr, text="Man",variable=gender,value=1)
rb1.pack()
rb2 = Radiobutton(fr, text="unMan",variable=gender,value=2)
rb2.pack()

cb = Checkbutton(win,text="send")
cb.grid(row=3, column=0)

btn = Button(win,text="enter",command=hello)
btn.grid(row=4,column=0,columnspan=2)


win.mainloop()