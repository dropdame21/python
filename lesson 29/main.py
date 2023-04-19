from tkinter import *

window = Tk()
window.geometry("400x400")
# def fgh(a):
#     print(znach1.get())
#
# def gfh(b):
#     print(znach2.get())
#
# def radi():
#     print(rb_val.get())
# znach1 = BooleanVar()
# znach2 = BooleanVar()
# chek1 = Checkbutton(window,text="яяяяяяяяяя",variable=znach1,onvalue=True,offvalue=False)
# chek2 = Checkbutton(window,text="oofhesevubivsbubuev",variable=znach2,onvalue=True,offvalue=False)
# chek1.bind("<Button-3>",fgh)
# chek2.bind("<Button-3>",gfh)
# chek1.pack()
# chek2.pack()
# rb_val = IntVar()
# rad = Radiobutton(window,variable=rb_val,text="1",value=67,command=radi).pack()

# def pupu():
#     print(lst.curselection())
#
# mas = ["ак47","Т-34","Т-72","Су-71"]
#
# lst = Listbox(window,selectmode=EXTENDED)
# lst.pack()
# for elem in mas:
#     lst.insert("end",elem)
#
# btn = Button(window,text="Activation",command=pupu).pack()
# def get_scale(e):
#     print(scale.get())
#
# scale = Scale(window,from_=4,to=16,orient=HORIZONTAL,length=200,width=200,tickinterval=2,command=get_scale)
# scale.pack()
# def qwe():
#     if btn1['state'] == "disabled":
#         btn1['state'] = "normal"
#     else:
#         btn1['state'] = "disabled"
#
# btn2 = Button(window, text="buy",command=qwe)
# btn1 = Checkbutton(window,text="on/off")
# btn1.select()
# btn1.pack()
# btn2.pack()
# def ag():
#     if val_sa.get() == 1:
#         lb['text'] = "Hello World"
#     else:
#         lb['text'] = "Hello Python"
#
# val_sa = IntVar()
# lb = Label(window,text="Hello...")
# rb1 = Radiobutton(window,text="World",value=1,variable=val_sa,command=ag)
# rb2 = Radiobutton(window,text="Python",value=2,variable=val_sa,command=ag)
# lb.pack()
# rb1.pack()
# rb2.pack()


# mas = ['red','green',"blue",'purple','pink','gold']
# def fg(e):
#     root.config(background=mas[val.get()])


# val = IntVar()
# ck = Scale(root,from_=0,
#            to=5,
#            variable=val,
#            command=fg,
#            orient=HORIZONTAL)
# ck.pack()
def bold():
    if val_bold.get():
        lab['font'] += " bold"
    else:
        lab['font'] = lab['font'].replace(" bold", "")

def italic():
    pass

lab = Label(window,text="efi",font="Arial 15")
lab.pack()

val_bold = BooleanVar()
cb_bold = Checkbutton(window,text="jirniy",command=bold,variable=val_bold,onvalue=True,offvalue=False)
cb_bold.pack()
#============================
val_italic = BooleanVar()
cb_italic = Checkbutton(window,text="cursiv",command=italic,variable=val_italic,onvalue=True,offvalue=False)
cb_italic.pack()

window.mainloop()