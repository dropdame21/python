from tkinter import*
def hell_o(a):
    print("Swinka zarezana")
    print(a)

def show_message():
    label['text'] = okn.get()
    okn.delete(0,'end')


root = Tk()
label = Label(text="chmo")
label.grid(row=5,column=6)
photota = PhotoImage(file='pig.png')
root.title('uvuirifugru')
root.geometry('800x700')
lb = Label(root, text="Hi!",font='Times 30')
lb.grid(column=0,row=0)
# btn = Button(root,bg='black',fg='pink')
# btn.grid(column=2,row=0)
# btn['command'] = hell_o
# btn['text'] = 'swinka'
# btn['font'] = ('times new roman', 20,'bold')
# btn['height'] = 2
# btn['width'] = 5
lb1 = Label(root,image=photota)
lb1.grid(column=3,row=0)

btn1 = Button(root,bg='black',fg='pink')
btn1.bind('<Button-1>',hell_o)
btn1.grid(column=4,row=0)
btn1['text'] = 'swinota'
btn1['font'] = ('times new roman', 20,'bold')
btn1['height'] = 2
btn1['width'] = 5
btn2 = Button(root,image=photota)
btn2.grid(column=2,row=2)

okn = Entry(root)
confirm = Button(text="Enter",command=show_message)
confirm.grid(row=4,column=5)
okn.grid(row=4,column=4)




root.mainloop()