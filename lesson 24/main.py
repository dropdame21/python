# class FiftiFifti:
#     def __init__(self):# магическое
#         self.money = 0.05 # public
#         self.__zarplata = 20000 # private
#     def ipotek(self):
#         if self.__zarplata > 75000: # использование приватных данных
#             return True
#         else:
#             return False
#     def povishenie(self): # public
#         self.__zarplata += 3000
#
#     def __bar(self): # private
#         return  True
#
#     def gou(self):
#         if self.__zarplata > 3:
#             print(self.__bar())
#
#     def greet(self):# обычное
#         print("hi")
#
# sany = FiftiFifti()
# print(sany.money)
# sany.greet()
# sany._FiftiFifti__zarplata = 21000 # private
# print(sany._FiftiFifti__zarplata)
# sany.povishenie()
# print(sany.ipotek())
# sany.povishenie()
# print(sany.ipotek())
# sany.gou()

#
# class Car:
#     def __init__(self):
#         self.status = 0
#     def start(self):
#         if self.status == 1:
#             print("uje")
#         else:
#             self.status = 1
#             print("Запустился")
#     def stop(self):
#         if self.status == 0:
#             print("uje")
#         else:
#             self.status = 0
#             print("Заглох")
#     def t(self,type):
#         self.t = type
#         print(self.t)
#     def c(self,color):
#         self.c = color
#         print(self.c)
#     def y(self,year):
#         self.y = year
#         print(self.y)
# toyota = Car()
# toyota.t("supra")
# toyota.c("orange")
# toyota.y("1996")
# toyota.start()
# toyota.stop()
# import string
#
# class Alfabet():
#     def __init__(self):
#         self.__leter = string.ascii_lowercase
#         self.__lang = "Eng"
#     def print(self):
#         print(self.__leter)
#
#     def letters_number(self):
#         print(len(self.__leter))
# asd = Alfabet()
# asd.print()
# asd.letters_number()


# import  datetime
#
# class Clocks():
#     def __init__(self):
#         self.__time = datetime.datetime.now().strftime("%H"+":"+"%M"+":"+"%S")
#         self.__h, self.__m, self.__s = self.__time.split(":")
#
#
#
# c = Clocks()
# print(c.h)

import random
class Blabla:
    def __init__(self):
        self.__counter = 5
    def increment(self):
        self.__counter += 1
    def decrement(self):
        self.__counter -= 1
    def ret(self):
        return self.__counter
counter = Blabla()
mas = [counter.increment,counter.decrement]
while 0 < counter.ret() <  10:
    random.choice(mas)()
    print(counter.ret())


# class Clocks:
#     def __init__(self):
#         self.__time = '23:59:59'
#         # self.__time = datetime.datetime.now().strftime("%H:%M:%S")
#         self.__h, self.__m, self.__s = self.__time.split(":")
#         self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
#     def __test_h(self):
#         if self.__h >= 24:
#             self.__h = 0
#     def __test_m(self):
#         if self.__m >= 60:
#             self.__m = 0
#             self.__h += 1
#
#     def __test_s(self):
#         if self.__s >= 60:
#             self.__s = 0
#             self.__m += 1
#     def hour(self):
#         self.__h = int(self.__h)+1
#         self.__test_h()
#     def min(self):
#         self.__m = int(self.__m) + 1
#         self.__test_m()
#         self.__test_h()
#     def sec(self):
#         self.__s = int(self.__s) + 1
#         self.__test_s()
#         self.__test_m()
#         self.__test_h()
#     def coc(self):
#         return f'{str(self.__h).rjust(2, "0")}:{str(self.__m).rjust(2, "0")}:{str(self.__s).rjust(2, "0")}'
# c = Clocks()
# c.sec()
# c.hour()
# c.min()
# print(c.coc())

