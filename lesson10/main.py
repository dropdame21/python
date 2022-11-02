#task1
# a = int(input())
# b = int(input())
# while a <= b:
#     print(a)
#     a += 1
# a = int(input())
# b = int(input())
# for i in range(b-a+1):
#     print(a)
#     a += 1

#task2

# a = int(input())
# print(' '*(a-1)+"⭐")
# for i in range(a):
#     b = i + 1
#     print(' '*(a-b)+'#'*(b*2)+' '*(a-b))
# print(" "*(a-1)+'||')
# for i in range(a):
#     b = i + 1
#     print('#'*(b))

#task3

# a = int(input())
# for i in range(10):
#     b = i + 1
#     print(a,'*',b,'=',4*b)

#task4

# a = int(input('высота: '))
# b = int(input('Ширина: '))
# for i in range(a):
#     print('#'*b)

#task5

a = '12345'
mas = []
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stages = stages[::-1]
for i in range(len(a)):
    mas.append(a[i])
print(mas)
massiv = ['_']*len(mas)
print(massiv)
for i in range(7):
    b = input()
    for j in range(len(mas)):
        if b == mas[j]:
            massiv[j] = b
    print(massiv)
    print(stages[i])
    if mas == massiv:
        print('you are win')
        break
if mas != massiv:
    print('you are lose')
