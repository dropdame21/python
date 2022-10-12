# surname = input()
# name = input()
# otchestvo = input()
# print(surname, name[0]+".", otchestvo[0]+".")
# surname = input().capitalize()
# name = input().capitalize()
# otchestvo = input().capitalize()
# print(surname, name[0]+".", otchestvo[0]+".")
# a = "abracadabra"
# print(a.count("a"))
# a = "Hellow, World !"
# mas = a.split(" ")
# mas.remove("!")
# mas.pop(0)
# print(mas[0])
# mas = {".":".",",":",","!":"!","?":"?"," ":" ","а":"a","б":"b","в":"v","г":"g","д":"d","е":"ye","ё":"yo","ж":"j","з":"z","и":"i","й":"y","к":"k","л":"l","м":"m","н":"n","о":"o","п":"p","р":"r","с":"s","т":"t","у":"u","ф":"f","х":"h","ц":"c","ч":"ch","ш":"sh","щ":"shy","ъ":"","ы":"i","ь":"'","э":"a","ю":"yu","я":"ya"}
# a = input()
# fraz = ''
# for i in range(len(a)):
#     b = a[i].isupper()
#     c = a[i]
#     if b == True:
#         c = c.lower()
#         d = mas[c]
#         d = d.upper()
#         fraz+= d
#     else:
#         fraz += mas[(a[i])]
# print(fraz)
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
a = int(input())
if a % 4 == 0 or (a % 100 and a % 400 == 0):
    print("Високостный")
else:
    print("Невисокостный")