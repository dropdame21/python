# n = 0
# while n != 1:
#     a = input().lower().strip()
#     b = input().lower().strip()
#     if a == 'yellow' and b == 'red':
#         print('orange')
#     elif a == 'yellow' and b == 'blue':
#         print('green')
#     elif a == 'red' and b == 'blue':
#         print("purple")
#     if b == 'yellow' and a == 'red':
#         print('orange')
#     elif b == 'yellow' and a == 'blue':
#         print('green')
#     elif b == 'red' and a == 'blue':
#         print("purple")
#     else:
#         print('errore')
#     n = int(input('do you want continue?'))




# a = int(input())
# b = int(input())
# c = int(input())
# for i in range(c):
#     print(f"{i+1} day, zombi: {a}")
#     a = a + a*b



# a = input()
# def ussr(lis):
#     mas = lis.split(' ')
#     massiv = []
#     for i in range(len(mas)):
#         ma = i+1
#         mi = i-1
#         if ma >= len(mas):
#             ma -= len(mas)
#         massiv.append(int(mas[mi])+int(mas[ma]))
#     return massiv
# print(ussr(a))


def reader(file):
    f = open(file,'r')
    c = f.read()
    g = c.split('\n')
    h = 0
    for i in range(len(g)):
        h+=len(g[i].split(" "))
    return len(c),len(g),h
print(reader('dfg.txt'))

