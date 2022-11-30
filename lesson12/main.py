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

list1 = ["Михаил", "", "Григорий", "Александр", "", "Степан"]
for i in range(len(list1)):
    if list1[i] == "":
        list1.pop(i)
print(list1)