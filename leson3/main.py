# a = input()
# print(len(a))
# a = "Пупсень"
# b = "Вупсень"
# c = "Кузя"
# mas = [a,b,c]
# print(mas[0][2:])
# path = "C:/ProgramData/Corel/Messages/540111125_707000/RU/MessageCache1/python.exe"
# mas=path.split('/')
# print(mas)
# print(mas[-1])
# file = mas[-1].split('.')
# print(file[1])
# print(mas[-2])
# lens = len(mas[-1])
# print(path[0:-lens])
# a = input("glava 1: ")
# a1 = input("stranica: ")
# b = input("glava 2: ")
# b1 = input("stranica: ")
# c = input("glava 3: ")
# c1 = input("stranica: ")
# print(a," "*(50-len(a)-len(a1)),a1)
# print(b," "*(50-len(b)-len(b1)),b1)
# print(c," "*(50-len(c)-len(c1)),c1)
# a = "12'345'678"
# mas = a.split("'")
# chisl = mas[0]+mas[1]+mas[2]
# chisl = int(chisl)
# print(chisl)
# print(type(chisl))
# a = input()
# if len(a)>= 3:
#     print(a[2])
# else:
#     print("третьего символа нет")
# print(a[-2])
# print(a[0:6])
# print(a[0:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))
# name = { "Антон": ["Йога", "Левый берег", "Разработка"] }
# print(name["Антон"][-1])
# print(name["Антон"][-1],"и",name["Антон"][0])
# a = input()
# print("_"*5+a+"_"*5)
# a = input()
# mas = a.split(" ")
# s = ''
# for i in range(len(mas)):
#     s+=mas[i][0]
# print(s)
a = input()
mas = a.split(" ")
mas[2]="Movavi"
s = ''
for i in range(len(mas)):
    s+=mas[i]+" "
print(s)