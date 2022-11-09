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

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
is_game = "y"
score = 0
while is_game == "y":
    computer = [random.choice(cards)]
    player = [random.choice(cards)]

    get_card = "y"
    while get_card == "y":
        player.append(random.choice(cards))
        if sum(player) > 21 and 11 in player:
            """если туз в руке и сумма > 21"""
            for i in range(0, len(player)):
                if player[i] == 11:
                    player[i] = 1
                    break
        score = sum(player)
        print(f"Твоя рука: {player}. Очков: {score}")
        print("Первая карта компьютера:", computer[0])
        if score > 21:
            get_card = "n"
        else:
            get_card = input("y - взять карту, n - остановиться: ")

        while sum(computer) < 17:
            computer.append(random.choice(cards))

        if sum(computer) > 21 and 11 in computer:
            """если туз в руке и сумма > 21"""
            for i in range(0, len(computer)):
                if computer[i] == 11:
                    computer[i] = 1
                    break
        score_computer = sum(computer)
        print("=" * 10)
        print(f"Твоя итоговая рука: {player}. Очков: {score}")
        print(f"Итоговая рука компьютера: {computer}. Очков: {score_computer}")

        if score > 21 and score_computer > 21:
            print("Перелёт у обоих. Ничья.")
        elif score > 21:
            print("Твой перелёт. Ты проиграл.")
        elif score_computer > 21:
            print("Перелёт компьютера. Ты победил.")
        elif score == score_computer:
            print("Ничья")
        elif score > score_computer:
            print("Победа.")
        else:
            print("Проиграл")

        is_game = input("Играем дальше? y - да, n - нет")