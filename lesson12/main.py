# lst1 = ["lo", "Mov"]
# lst2 = ["ve", "avi"]
# mas = []
# for i in range(len(lst1)):
#     mas.append(lst1[i]+lst2[i])
# print(mas)

#task2

# lst1 = ["Привет", "люблю"]
# lst2 = ["Мир", "солнышко"]
# mas = []
# for i in range(len(lst1)):
#     for j in range(len(lst2)):
#         mas.append(lst1[i]+' '+lst2[j])
# print(mas)

#task 3

# lst1 = [10, 20, 30, 40]
# lst2 = [100, 200, 300, 400]
# for i in range(len(lst1)):
#     print(lst1[i],' ',lst2[-(i+1)])

#task 4

# list1 = ["Михаил", "", "Григорий", "Александр", "", "Степан"]
# for i in range(len(list1)):
#     if list1[i] == "":
#         list1.pop(i)
# print(list1)

#task 4

# a = int(input())
# lst = [10, 20, 30, 40, [300, 400, 500, [5000, 6000]]]
# mas = lst[-1][-1]
# mas.append(a)
# print(lst)

#task 5

# partners = ["Мама", "Собака", "Моя тень"]
# partners_new = ["Apple", "Google", "Яндекс"]
# partners.extend(partners_new)
# print(partners)

#task 6

# lst = [5, 10, 15, 20, 25, 50, 20]
# lst[3]=200
# print(lst)

#task 7

# lst = [5, 10, 15, 20, 25, 50, 20]
# mas = []
# for i in range(len(lst)):
#     if lst[i] != 20:
#         mas.append(lst[i])
# print(mas)

#task 1

# a = int(input())
# b = int(input())
#
# mas = []
# for i in range(a+1,b):
#     mas.append(i**2)
# print(mas)

#task 2

# a = input()
# mas = a.split(' ')
# mas.reverse
# print(mas)

#task 3

# a = input('ввод: ')
# ch = 0
# nch = 0
# pop = 0
# while a != 'end':
#     if a.isdigit() == False:
#         pop+=1
#         print('А хотелось бы число...')
#     elif int(a) % 2 == 0:
#         ch += 1
#     else:
#         nch += 1
#     a = input('ввод: ')
# print("Чётных: ",ch)
# print("Нечётных: ",nch)
# print("Не чисел: ",pop)

#task 4

# a = input()
# mas = a.split(' ')
# for i in range(1,len(mas)):
#     if int(mas[i]) > int(mas[i-1]):
#         print(mas[i],'>',mas[i-1])

#task 5

# mas = [-5, 14, 2, -8, 1]
# a = min(mas)
# b = max(mas)
# c = mas.index(min(mas))
# d = mas.index(max(mas))
# mas[c] = b
# mas[d] = a
# print(mas)

# task 6
# from random import randint
#
# a = int(input('Сколько учеников в строю (от 5 до 20): '))
# b = int(input('Рост Пети: '))
# rosty = []
# for i in range(a):
#     rosty.append(randint(150,200))
# rosty.append(b)
# rosty.sort(reverse=True)
# v = rosty[::-1]
# c = len(v) - (v.index(b))
# print(rosty)
# print('vashe mesto u parashy, a vovino : ',c)

# task 7

# a = int(input())
# rev = [4, 5, 6, 7, 8, 9, 0]
# mas = [4, 5, 6, 7, 8, 9, 0]
# for i in range(len(mas)):
#     if len(mas) <= i+a:
#         rev[i+a-len(mas)] = mas[i]
#     else:
#         rev[i+a] = mas[i]
# print(rev)
