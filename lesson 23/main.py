import random
# class Apop:
#     def __init__(self, age , name, surname, grades):
#         self.age = age
#         self.name = name
#         self.surname = surname
#         self.grades = grades
#         self.sr = sum(grades) / len(grades)
#     def __str__(self):
#         return(f"I am {self.name} {self.surname} and i {self.age} years old")
#     def greet(self):
#         return(f"gegugyyr. I am {self.name} {self.surname} and i {self.age} years old")
# n = [random.randint(2,5) for i in range(2,10)]
# greta = Apop(123,"greta","tumbochka",[random.randint(2,5) for i in range(2,10)])
# treta = Apop(123,"treta","tumbochka",[random.randint(2,5) for i in range(2,10)])
# sreta = Apop(123,"sreta","tumbochka",[random.randint(2,5) for i in range(2,10)])
# freta = Apop(123,"freta","tumbochka",[random.randint(2,5) for i in range(2,10)])
# kreta = Apop(123,"kreta","tumbochka",[random.randint(2,5) for i in range(2,10)])
# students = [greta, treta, sreta, freta, kreta]
# d = {}
# for i in students:
#     d[i.name] = i.sr
# sorted_tuples = sorted(d.items(), key=lambda item: item[1])
# sorted_dict = {k: v for k, v in sorted_tuples}
# print(d)
# print(sorted_tuples)


#task 4


class Wall:
    def __init__(self, width):
        self.width = width
        self.height = random.randint(3,7)
    def print_figure(self):
        breek = """\n _\n|_|"""
        for i in range(self.height):
            print(breek*self.width)

df = Wall(3)
print(df.print_figure())

# ntitled
# A
# GUEST
# MAR
# 8
# TH, 2023
# 1
# 0
# NEVER
# ADD
# COMMENT
# Not
# a
# member
# of
# Pastebin
# yet? Sign
# Up, it
# unlocks
# many
# cool
# features!
# 3.62
# KB | None |

# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#
#     def __str__(self):
#         return "Бархат, кефтеме"
#
#
# leha = Person("Лёха", 0)
#
# print(leha)
# print(leha.age)
# print(leha.name)

# class Kefteme:
#     def __getitem__(self, item):
#         print("Подкрадули кротячьи. Я ставлю тебе", item)
#
# obj = Kefteme()
# obj[2]


# zadacha 1
# class Zxcvoin:
#     def __init__(self, age, name, surname):
#         self.age = age
#         self.name = name
#         self.surname = surname
#     def __str__(self):
#         return(f'Я {self.name} {self.surname} и мне {self.age}')
#     def greet(self):
#         return (f'ай сау братка. Я {self.name} {self.surname} и мне {self.age}')
# sf = Zxcvoin(67, 'андрей', 'иммерсион')
# # print(sf.age)
# # print(sf.name)
# # print(sf.surname)
# print(sf.greet())

# z2
# import random
# class Zxcvoin:
#     def __init__(self, age, name, surname, grades):
#         self.age = age
#         self.name = name
#         self.surname = surname
#         self.grades = grades
#         self.sr = sum(grades) / len(grades)
#     def __str__(self):
#         return(f'Я {self.name} {self.surname} и мне {self.age}')
#     def greet(self):
#         return (f'ай сау братка. Я {self.name} {self.surname} и мне {self.age}')
# anna = Zxcvoin(123, 'аня', 'старперка', [random.randint(2, 5) for i in range(2, 10)])
# mana = Zxcvoin(123, 'маня', 'лошпедус', [random.randint(2, 5) for i in range(2, 10)])
# sana = Zxcvoin(123, 'саня', 'чмище', [random.randint(2, 5) for i in range(2, 10)])
# dana = Zxcvoin(123, 'даня', 'дотер', [random.randint(2, 5) for i in range(2, 10)])
# vana = Zxcvoin(123, 'ваня', 'зхцвоин', [random.randint(2, 5) for i in range(2, 10)])
# students = [anna, mana, sana, dana, vana]
# # d = {anna: anna.sr,
# #      mana: mana.sr,}
# d = {}
# for j in students:
#     d[j.name] = j.sr
# sorted_tuples = reversed(sorted(d.items(), key=lambda item: item[1]))
# sorted_dict = {k: v for k, v in sorted_tuples}
# print(d)
# print(sorted_dict)


# 3, 4


# class Popoint:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"It is X:{self.x}, It is Y:{self.y}"
#
#
# class Rectalnoe:
#     def __init__(self):
#         self.xyz1 = gg
#         self.xyz2 = ggvp
#     def ploshad(self):
#         a = self.xyz2.x - self.xyz1.x
#         b = self.xyz2.y - self.xyz1.y
#         return a*b
#     def perimetr(self):
#         a = self.xyz2.x - self.xyz1.x
#         b = self.xyz2.y - self.xyz1.y
#         return (a+b)*2
#     def haspoint(self,kok):
#         if (self.xyz1.x <= kok.x <= self.xyz2.x) and (self.xyz1.y <= kok.y <= self.xyz2.y):
#             return True
#         else:
#             return not True
#
#
# gg = Popoint(1,142)
# ggvp = Popoint(2,154)
# barhat = Popoint(2,150)
# print(gg,ggvp)
# tp = Rectalnoe()
# print(tp.ploshad())
# print(tp.perimetr())
# print(tp.haspoint(barhat))

# задача 5
import random


class Wall:
    def __init__(self, width):
        self.width = width
        self.height = random.randint(3, 7)

    def print_figure(self):
        d = '''⬛'''
        for i in range(self.height):
            print(self.width * d)


obj = Wall(width=2)
obj.print_figure()

