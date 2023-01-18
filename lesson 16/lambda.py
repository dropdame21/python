#task 1

c2f = lambda C: 9/5 * C + 32

f2c = lambda F: (F - 32)* 5/9

c2k = lambda C: C + 273.15

k2c = lambda K: K - 273.15

k2f = lambda K: 9/5 * (K - 273.15 ) + 32

f2k = lambda F: (F - 32)* 5/9 + 273.15
print(f2k(203))