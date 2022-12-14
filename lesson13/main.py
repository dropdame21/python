from random import randint
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# print(set1|set2) # .union(Пересечение)
# print(set1&set2) # .intersrction(Объединение)
# print(set1-set2)# ,difference(разность)
# print(set1 ^ set2)# symmetric_difference(симметрическая разность)

#task 1
#
#
# mas = []
# for i in range(5):
#     mas.append(randint(1,10))
# print(mas)
# set = set(mas)
# if len(set)%10 > 5 or len(set)%10 == 0:
#     print(len(set),"штук:",set)
# else:
#     print(len(set),"штуки:",set)

#task 2

# mas = []
# mas2 = []
# size = randint(100,1000)
# for i in range(size):
#     mas.append(randint(0,10000))
#     mas2.append(randint(0, 10000))
# set1 = set(mas)
# set2 = set(mas2)
# mas = list(set1|set2)
# print("Общих чисел: ",len(set1&set2))
# print("Общих чисел: ",size)
# print("[Максимальное значение]: ",max(mas))
# print("[Минимальное значение]: ",min(mas))
# print(sorted(mas))

#task 3

# a = input("Ввод: ")
# mas = []
# while a != 'end':
#     if a.lstrip("-").isdigit():
#         if a in mas:
#             print("✅ ДА")
#         else:
#             mas.append(a)
#             print("❌ НЕТ")
#     else:
#         print("⚠️ Число нужно!")
#     a = input("Ввод: ")

#task 4

# lst1 = [0, False, 1 - 1, "один", 2, 3.14]
# mas = set(lst1)
# n = list(mas)
# itog = []
# print(lst1,"- Возможно есть повторение")
# print(mas,"- повторений нет.")
# if len(lst1) != len(mas):
#     print("=> Дубликаты есть.")
# else:
#     print("=> Дубликатов нет.")

#task 5

# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', ',', '.', '?', '>', '<', "'", '"', '/', ':', ';']
# a = input()
# a = a.lower()
# itog = ""
# for i in a:
#     if i not in symbols:
#         itog += i
# a = itog.split(" ")
# set = set(a)
# print(a)
# print(set)
# print(len(set))

#task 1

a = int(input())
dict = {}
for i in range(a):
    b , a = input().upper().split(" ")
    if b not in dict:
        dict[b] = [a]
    else:
        dict[b].append(a)
print(dict)
