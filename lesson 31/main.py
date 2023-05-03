from tkinter import *


window = Tk()

window.geometry("550x550")
# c = Canvas(window,width=500,height=500,bg = "Yellow")
# c.pack(anchor=CENTER,expand=True)
# c.create_text(100,100,text="Кефтеме🦿😈",font="Arial 24 italic",fill="green",anchor=NW)
# # c.create_rectangle(90,60,410,440,fill="pink",outline="blue3",width=30)



#task 1
#
#
# a = 0
# def hellow():
#     global a
#     c.delete("all")
#     c.create_text(250, 250, text=str(a), fill="black", font="50", anchor=NW)
#     a+=1
#     window.after(1000,hellow)
#
# c = Canvas(window,width=500,height=500)
# c.pack(anchor=CENTER,expand=True)
# pt = PhotoImage(file="235883976-54791470-eaa6-475d-9a81-8bfe3afe5014.png")
# c.create_image(10,10,anchor=NW,image=pt)
# hellow()


#task 2


global a
global b
a = None
b = None
c = Canvas(window,width=200,height=200,bg="white")
c.pack(anchor=CENTER, expand=1)
def lkm(event):
    global a
    a = (event.x,event.y)

def pkm(event):
    global b
    b = (event.x,event.y)

c.bind("<Button-1>",lkm)
c.bind("<Button-3>",pkm)


def cre():
    if a and b:
        c.delete("all")
        c.create_line(a[0], a[1], b[0], b[1])

btn = Button(window,text="create line",command=cre)
btn.pack()




window.mainloop()
