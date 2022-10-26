# import art
# import random
# a = int(input("Напиши 0 для КАМНЯ, 1 для БУМАГИ, 2 для НОЖНИЦ: "))
# if a > 2 or a < 0:
#     print("--------------")
#     print("Ты написал неверное число. Ты проиграл!")
# else:
#     print("[твой выбор]")
#     print(art.figures[a])
#     b = random.randint(0,2)
#     print("[выбор компьютера]")
#     print(art.figures[b])
#     if a == b:
#         print("Ничья")
#     elif a == 1 and b == 2:
#         print("you lose")
#     elif a == 2 and b == 3:
#         print("you lose")
#     elif a == 3 and b == 1:
#         print("you lose")
#     else:
#         print("you win")
#--------------------------------------------------

# ints = []  # список для того чтобы помещать в него все числа
# try:
#    f = open('1.txt')  # помещаем файл в переменную для того чтобы работать с ним
#    try:
#       for line in f:  # проходимся по каждой строке внутри файла
#          ints.append(int(line))# добавляем в список строку преобразованное в число
#          if line < 5:
#             print(line)
#    except ValueError:  # если будет ошибка и будет попытка обработать не число
#       print('Это не число. Выходим.')
#    else:  # если ошибок не было
#       print('Всё хорошо.')
#    finally:  # в любом случае
#       f.close()  # закрываем файл
#       print('Я закрыл файл.')
# except:
#    print("file not found")
#--------------------------------------------
#
# a = input()
# b = input()
# try:
#    a = int(a)
#    b = int(b)
#    try:
#       print(a / b)
#    except:
#       print("Are you sure?")
# except:
#    print("it is fun, but it's not int type")

#----------------------------------------------------------

# import random
# while True:
#     print("Угадай число")
#     mini = 0
#     maxi = 0
#     computer_number = random.randint(0, 100)
#     life = 7
#     while life > 0:
#        try:
#         user_number = int(input("Введи число: "))
#         if user_number < 0 or user_number > 100:
#             print("Введи число от 0 до 100")
#             continue
#         if computer_number == user_number:
#             print("Вы победили!")
#             break
#         elif computer_number < user_number:
#             print("Нужно меньше.")
#             maximum = user_number
#         else:
#             print("Нужно больше.")
#             minimum = user_number
#             print(f">>> Интервал: {mini} – {maxi}")
#             life = life - 1
#             print("❤️:", life)
#        except:
#            print("it is not int type")
#     answer = input("Хочешь продолжить?")
#     if answer == "Да":
#         continue
#     else:
#         break

#-------------------------------------------------------------------------

