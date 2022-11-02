import arts
from random import randint
# #task1
# a = 7
# while a < 100:
#     print(a)
#     a += 7

# #task2
#
# a = input()
# while len(a) > 0:
#     print(a)
#     a = a[:-1]

#task3

# a = int(input())
# b = 0
# while b < a:
#     print(b)
#     b += 2

#task4


# kolvo = 0
# summa = 0
# a = input('Ввод: ')
# c = float(a)
# minimal = c
# maximal = c
# while a != 'end':
#     c = float(a)
#     summa += c
#     kolvo += 1
#     if c < minimal:
#         minimal = c
#     if c > maximal:
#         maximal = c
#     a = input('Ввод: ')
# print(f"[Дублонов потрачено]: {summa}\n[Покупок]: {kolvo}\n[Максимум]: {maximal}\n[Минимум]: {minimal}")

#task5

# a = int(input('Ввод: '))
# b = 0
# while a > 1:
#     if a % 2 == 0:
#         print(b + 1,')',a,'/ 2 =',a//2)
#         a = a // 2
#     else:
#         print(b + 1,')',a,'* 3 + 1 =',a * 3 + 1)
#         a = a * 3 + 1
#     b += 1
# print('Шагов',b)

#task6

# print(arts.logo)
# a = input()
# summa = int(a)
# a = input()
# while a != "=":
#     b = a[0]
#     a = a[1:]
#     a = int(a)
#     if b == "^":
#         print(f"Уравнение: {summa}{b}{a}")
#         summa=summa**a
#         print(f"Ответ: {summa}")
#     elif b == "*":
#         print(f"Уравнение: {summa}{b}{a}")
#         summa=summa*a
#         print(f"Ответ: {summa}")
#     elif b == "/":
#         print(f"Уравнение: {summa}{b}{a}")
#         summa=summa//a
#         print(f"Ответ: {summa}")
#     elif b == "-":
#         print(f"Уравнение: {summa}{b}{a}")
#         summa=summa-a
#         print(f"Ответ: {summa}")
#     else:
#         print(f"Уравнение: {summa}{b}{a}")
#         summa=summa+a
#         print(f"Ответ: {summa}")
#     a = input()
# print(f"Итоговый ответ: {summa}")

#dop task1

a = input("y or n: ")
player = []
diller = []
if a == 'y':
    player.append(randint(1,10))
    player.append(randint(1,10))
    diller.append(randint(1,10))
    diller.append(randint(1,10))
    a = input()
    while a != '-' and sum(player) <= 21:
        player.append(randint(1, 10))


else:
    print()