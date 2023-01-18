from pictures import box_carrot,box_close,box_empty
from random import choice



def generation_boxes(stata1,stata2):
    result = ''
    if stata1 == 'PUSTOTA':
        boxic1 = box_empty.format(COLOR1.center(13)).split('\n')
    elif stata1 == 'CARROT':
        boxic1 = box_carrot.format(COLOR1.center(13)).split('\n')
    else:
        boxic1 = box_close.format(COLOR1.center(13)).split('\n')

    if stata2 == 'PUSTOTA':
        boxic2 = box_empty.format(COLOR2.center(13)).split('\n')
    elif stata2 == 'CARROT':
        boxic2 = box_carrot.format(COLOR2.center(13)).split('\n')
    else:
        boxic2 = box_close.format(COLOR2.center(13)).split('\n')

    for element in zip(boxic1, boxic2):
        result += "   ".join(element) + "\n"
    result += name1[:10].center(13) + " " * 7 + name2[:10].center(13)
    return result

COLORS = ['ФИОЛЕТОВАЯ','КАЙФОВАЯ','МАГАДАНСКАЯ','УНЫЛАЯ']
COLOR1 = choice(COLORS)
COLOR2 = choice(COLORS)

while COLOR1 == COLOR2:
    COLOR2 = choice(COLORS)

box1 = 'Closed'
box2 = 'closed'




name1 = input('name1 = ')
while name1.strip(' ') == '':
    print('ty down')
    name1 = input('name1 = ')
name2 = input('name2 = ')
while name2.strip(' ') == '':
    print('ty down')
    name2 = input('name1 = ')


print(generation_boxes("PUSTOTA","chtoto"))

while True:
    print(f"{name2}, в твоей коробке {box2}")
    action = input(f"Нужно сделать выбор: \n"
                   f"1.Блеф: сказать что в коробке {box1}\n"
                   f"2.Блеф: сказать что в коробке {box2}\n"
                   f">>> (Б - блефб П - правда) -> ").upper()
    while action != "Б" and action != "П":
        action = input(f">>> (Б - блеф, П- правдв) -> ").upper()
    print("\n"*100)
    input(f">>> {name1} открывает глаза(Enter)...")
    if action == "Б":
        print(f"{name2} сообщает, что в его коробке {box1}")
    else:
        print(f"{name2} сообщает, что в его коробке {box2}")

    change = input("menayechsya (yes) ili net (no)?")
    if change == "yes":
        box1,box2 = box2,box1
        input(f"{name1} close your glaza")

        if box2 == 'CARROT':
            boxic2 = box_carrot.format(COLOR2.center(13)).split('\n')
        else:
            boxic2 = box_empty.format(COLOR2.center(13)).split('\n')
    else:
        break
print("======================= resultat ========================")
print(generation_boxes(box1,box2))
if box1 == "CARROT":
    print(name1,"is winner")
else:
    print(name2,"is winer")
