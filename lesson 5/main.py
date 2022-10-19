# #задача 1
# a = int(input("Введите число: "))
# if a == 0:
#     print("Число равно нулю")
# elif a > 0:
#     print(f"Число {a} положительное")
# else:
#     print(f"Число {a} отрицательное")
# #task 2
# a = int(input("write year: "))
# if a % 4 == 0 and (a % 400 == 0 or a % 100 != 0):
#     print(f"{a} год високосный")
# else:
#     print(f"{a} год не високосный")
# #task 4
# pol = 0
# otr = 0
# for i in range(3):
#     a = int(input("Введите число: "))
#     if a > 0:
#         pol+=1
#     elif a < 0:
#         otr+=1
# print("положительных:", pol)
# print("Отрицательных:", otr)
# #task 5
# mas = []
# for i in range(3):
#     a = int(input("Введите число: "))
#     mas.append(a)
# print("Максимальное:",max(mas))
# print("Минимальное:",min(mas))
# #task 6
# errore = 0
# a = int(input("hours: "))
# b = int(input("minutes: "))
# c = int(input("seconds: "))
# if a <= 24 and b <= 60  and a <= 60:
#     print("Время введено верно")
#     if a < 10:
#         if b < 10:
#             if c < 10:
#                 print(f"0{a}:0{b}:0{c}")
#             else:
#                 print(f"0{a}:0{b}:{c}")
#         else:
#             if c < 10:
#                 print(f"0{a}:{b}:0{c}")
#             else:
#                 print(f"0{a}:{b}:{c}")
#     elif b < 10:
#         if c < 10:
#             print(f"{a}:0{b}:0{c}")
#         else:
#             print(f"{a}:0{b}:{c}")
#     elif c < 10:
#         print(f"{a}:{b}:0{c}")
#     else:
#         print(f"{a}:0{b}:{c}")
# else:
#     print("Время введено не верно")
# #task 7
# a = input("введите номер билета: ")
# b = a[-3:]
# c = a[:3]
# sum1 = 0
# sum2 = 0
# for i in range(3):
#     sum1+=int(b[i])
#     sum2 += int(c[i])
# if sum1 == sum2:
#     print("билет счастливый")
# else:
#     print("билет несчастливый")
# #dop task 1
# a = int(input())
# if 10 < a % 100 < 20:
#     print(f"{a} хомяков")
# elif a % 10 == 1:
#     print(f"{a} хомяк")
# elif 1 < a % 10 < 5:
#     print(f"{a} хомяка")
# else:
#     print(f"{a} хомяков")
# #dop task 2
# a = input()
# b = input()
# c = 0
# if len(a) == len(b):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] == b[i]:
#                 c+=1
#     if c == len(a):
#         print("yes")
#     else:
#         print("no")
# else:
#     print("no")
# #dop task 3
# a = input()
# b = input()
# a = a.lower()
# b = b.lower()
# c = 0
# if len(a) == len(b):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] == b[i]:
#                 c+=1
#     if c == len(a):
#         print("yes")
#     else:
#         print("no")
# else:
#     print("no")
# a = input()
# b = input()
# a = a.lower()
# b = b.lower()
# a = sorted(a)
# b = sorted(b)
# if a == b:
#     print("yes")
# else:
#     print("no")
#
# print(len("Wednesday, June 05, 2019 3:28:14 PM"))
#-----------
# #task 1
# a = input()
# if a.isdigit():
#     if 0 < a < 3 or a == 12:
#         print("winter")
#     elif 2 < a < 6:
#         print("vesna")
#     elif 5 < a < 9:
#         print("summer")
#     else:
#         print("otem")
#task 2
# a = 0
# print("за кого голосовал?")
# print("1.Единая Россия  2. Единая Россия\n3.Единая Россия  4.Единая Россия")
# b = int(input("tvoy otvet: "))
# if b == 1:
#     a+=1
#     print("Ты прав и получаешь очко")
# else:
#     a+=1
#     print("Ты прав и получаешь очко")
# print("-----------------------------------------")
# print("Кто самый лучший президент?")
# print("1.Путин  2.Путин\n3.Путин  4.Путин")
# b = int(input("tvoy otvet: "))
# if b == 2:
#     a+=1
#     print("Ты прав и получаешь очко")
# else:
#     a+=1
#     print("Ты прав и получаешь очко")
# print("-----------------------------------------")
# print("ты меня уважаешь?")
# print("1.Да  2.Нет\n3.Возможно  4.Я не знаю")
# b = int(input("tvoy otvet: "))
# if b == 1:
#     a += 1
#     print("Ты прав и получаешь очко")
# else:
#     print("Вы потеряли все хп от удара тупым предметом(предположительно стеклянной бутылкой) по голове")
# print("-----------------------------------------")
# if a == 3:
#     print("Поздравляю! ты выжил и сохранил очко")
#dop task 2
print("Напиши 0 для КАМНЯ, 1 для БУМАГИ, 2 для НОЖНИЦ: 1")
a = int(input())
ris = {}
