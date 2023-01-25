# import time
# import random
# from openpyxl import load_workbook
#
#
# t = random.randint(1,5)
# input("Нажмите Enter чтобы начать...")
#
# time.sleep(t)
# a = time.time()
# input("fire\n")
# b = time.time()
# c = b - a
# c = round(c,4)
# if c < 0.01:
#     print("ты мох")
# elif c < t + 0.6:
#     print("you are good sniper, your time",c)
# else:
#     print('your time:',c,'you are death')
# c = str(c)
# name = input('write your name please')
# fn = 'dan.xlsx'
# wb = load_workbook(fn)
# ws = wb['Sheet1']
# ws.append([name,c])
# wb.save(fn)
# wb.close()

#task 2
from random import randint

a = int(input("Напиши если не чмошка"))
fir = {}
for i in range(a, 6 * a + 1):
    fir[i] = 0
for _ in range(1_000_001):
    d = 0
    for _ in range(a):
        d += randint(1, 6)
    fir[d] += 1
print('Броски-Количество-Вероятность')
for i in fir:
    print(i, "чёрточка", fir[i], "Чёрточка", round((fir[i] / 1000_000) * 100, 2), "%")






