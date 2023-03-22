import random
from tkinter import *
class Human:
    default_name = "loh"
    default_age = "1"
    skidka = random.randint(5,20)
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__house = False
        self.__money = money
    def info(self):
        return self.age,self.name,self.__house,self.__money
    def earn_money(self,prib):
        self.__money += prib
    def default_info(self):
        return Human.default_age,Human.default_name
    def make_deal(self, dom):
        self.__house = dom._area
        self.__money -= dom.final_price(Human.skidka)
    def buy_house(self, dom):
        __price = dom.final_price(Human.skidka)
        if __price <= self.__money:
            asd.make_deal(dom)
            dom.owner = "it is house of",self.name
        else:
            print("у тебя мало денег, ты нищеброд и не можешь позволить себе дом")

class House:
    def __init__(self,area,price):
        self._price = price
        self._area = area
    def final_price(self,skidka):
        return (self._price / 100)*skidka


def clicked(asd):
    lbl = Label(window, text=asd.info())
    lbl.grid(column=2, row=2)
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')

txt = Entry(window,width=10)
txt.grid(column=1, row=0)
txt.focus()
asd = Human(txt.get(),"99",99999)
btn = Button(window, text="Enter",command=clicked(asd))
btn.grid(column=2, row=0)
window.mainloop()
print(asd.info())
asd.earn_money(99900)
print(asd.info())
print(asd.default_info())
dom = House("oefjiejfi",90)
asd.buy_house(dom)
print(asd.info())

