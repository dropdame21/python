m = '''
   _____________
  /            /|
 /            / |
 -------------  |
|{}| |
|  Коробка    | /
|             |/
 -------------
'''
mn = '''
         ||
         ||
   _____________
  /            /|
 /            / |
 -------------  |
|{}| |
|  Коробка    | /
|             |/
 -------------
'''
mc = '''
             ____________
            /            /
           /            /
           _____________
          /            /|
         /            / |
         -------------  |
        |             | |
        |  Коробка    | /
        |             |/
         -------------
        '''
def arc(color,sost):
    mas = []
    if sost == 1:
        return m.format(color+(' '*(13-len(color))))
    elif sost == 2:
        return mc
    else:
        return mn.format(color+(' '*(13-len(color))))

a = int(input())
# b = int(input())
# for i in range(2):
#     print(arc(a,b),sep=' ')

def chis(a):
    k = 0
    for i in range(2,a+1):
        if a % i == 0:
            k+=1
    if k == 1:
        return 'prostoe'
    else:
        return 'neprostoe'


print(chis(a))