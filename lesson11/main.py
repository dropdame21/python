# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# c = [' ','!',',',';',':','?','.','@','#','$']
# alphabet_2 = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP'''''''  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#
#            88             88
#            ""             88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP''''''' 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88
# """
# print(logo)
# a = input('')
# b = int(input())
# r = input()
# d = 0
# itog = ''
# if r == 'r':
#     if b >= len(alphabet_2):
#         print('Смешно, попробуй ещёраз')
#     else:
#         for i in range(len(a)):
#             for j in range(len(c)):
#                 if a[i] == c[j]:
#                     itog += a[i]
#                 else:
#                     d += 1
#             if d == 10:
#                 if (alphabet_2.index(a[i])) + b > len(alphabet_2):
#                     itog += alphabet_2[((alphabet_2.index(a[i])) + b) - len(alphabet_2)]
#                 else:
#                     itog += alphabet_2[(alphabet_2.index(a[i])) + b]
#             d = 0
# elif r == 'e':
#     if b >= len(alphabet):
#         print('Смешно, попробуй ещёраз')
#     else:
#         for i in range(len(a)):
#             for j in range(len(c)):
#                 if a[i] == c[j]:
#                     itog+=a[i]
#                 else:
#                     d+=1
#             if d == 10:
#                 if (alphabet.index(a[i]))+b > len(alphabet):
#                     itog+=alphabet[((alphabet.index(a[i]))+b)-len(alphabet)]
#                 else:
#                     itog+=alphabet[(alphabet.index(a[i]))+b]
#             d = 0
#
# print(itog)

#task 2

# import os
# logo = '''
#                          ___________
#                          \         /
#                           )_______(
#                           |"""""""|_.-._,.---------.,_.-._
#                           |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                        .-------------.
#                       /_______________\\
# '''
# print(logo)
# c = ''
# f = {}
# maximum = 0
# winner = ''
# while c != 'no':
#     a = input()
#     b = input()
#     f[a]=b
#     v = b[0:]
#     v = int(v)
#     if maximum < v:
#         maximum = v
#         winner = a
#     c = input()
#     os.system('cls||clear')
# print(winner, maximum)

#task4
#
# a = input("Введи: ")
# mas = []
# bitmap = """
# ....................................................................
#    **************   *  *** **  *      ******************************
#   ********************* ** ** *  * ****************************** *
#  **      *****************       ******************************
#           *************          **  * **** ** ************** *
#            *********            *******   **************** * *
#             ********           ***************************  *
#    *        * **** ***         *************** ******  ** *
#                ****  *         ***************   *** ***  *
#                  ******         *************    **   **  *
#                  ********        *************    *  ** ***
#                    ********         ********          * *** ****
#                    *********         ******  *        **** ** * **
#                    *********         ****** * *           *** *   *
#                      ******          ***** **             *****   *
#                      *****            **** *            ********
#                     *****             ****              *********
#                     ****              **                 *******   *
#                     ***                                       *    *
#                     **     *                    *
# ....................................................................
# """
# g = bitmap.splitlines()
# for i in range(len(a)):
#     mas.append(a[i])
# k = 0
# print(g)
# for j in range(len(g)):
#     hgk = ''
#     hjk = g[j+1]
#     print(hjk)
#     for i in range(len(bitmap)):
#         if hjk[i] == ' ':
#             hgk + ' '
#         else:
#             hgk + mas[k]
#             k += 1
#         if k == len(a):
#             k = 0
#     print(hgk)

import datetime

MONTHS = (
"Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
DAYS = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
while True:
    year = input('year: ')
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break
while True:
    month = input('month: ')
    if month.isdigit() and int(month) > 0:
        month = int(month)
        break

calText = ""
calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

for i in range(7):
    calText += DAYS[i] + ' '
calText += '\n'
weekSeparator = ('+----------' * 7) + '\n'
blankRow = ('|          ') + '|\n'

currentDate = datetime.date(year, month, 1)
while currentDate.weekday() != 0:
    currentDate -= datetime.timedelta(days=1)

while True:
    calText += weekSeparator
    dayNumberRow = ''
    for i in range(7):
        dayNumberLable = str(currentDate.day).rjust(2)
        dayNumberRow += '|' + dayNumberLable + (' ' * 8)
        currentDate += datetime.timedelta(days=1)
    calText += "|\n"
    calText += dayNumberRow
    for i in range(3):
        calText += blankRow


    if currentDate.month != month:
        break
calText += weekSeparator
print(calText)

calendarik = 'calendar_{}_{}.txt'.format(month, year)
with open(calendarik, "w") as file:
    file.write(calText)
print('all is save in ' + calendarik)