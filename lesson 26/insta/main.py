from klass import Person
import random


def prez():
    print(f"login: {us.login}")
    print(f"name: {us.name}")
    print(f"surname: {us.surname}")
    print(f"posts: {us.posts}")

def select_user():
    global us
    while True:
        us = random.choice(users)
        if us.login != current.login:
            break

def session():
    select_user()
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
            select_user()
        elif answer == "SUBSCRIBE":
            current.subscribe += 1
            us.subsscribers += 1









a = Person(name="Michgan",surname="Pavlovetc",login="DropDame",password="qwe123")
b = Person()
c = Person()
users = [a,b,c]
l = input("login: ")
p = input("password: ")
for i in users:
    if i.log_in(l,p) == True:
        current = i
        session()
print(a.name)
