from klass import Person
import random


def prez():
    us = random.choice(users)
    print(f"login: {us.login}")
    print(f"name: {us.name}")
    print(f"surname: {us.surname}")
    print(f"posts: {us.posts}")

def session():
    while True:
        prez()
        print("""[Возможные действия]: 
    - ПОДПИСКИ (посмотреть на кого подписан Ибрагим)
    - ПОДПИСЧИКИ (посмотреть кто подписан на Ибрагима)
    - ПОДПИСАТЬСЯ (стать подписчиком)
    - СЛЕДУЮЩИЙ аккаунт""")
        answer = input("> ".upper())
        if answer == "OUT":
            break
        elif answer == "СЛЕДУЮЩИЙ":
            pass





a = Person(name="Michgan",surname="Pavlovetc",login="DropDame",password="qwe123")
b = Person()
c = Person()
users = [a,b,c]
l = input("login: ")
p = input("password: ")
for i in users:
    if i.log_in(l,p) == True:
        session()
