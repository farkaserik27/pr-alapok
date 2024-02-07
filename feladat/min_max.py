"""
A szélsőérték meghatározása esetében azt vizsgáljuk, hogy melyik a legkisebb,
illetve a legnagyobb érték az adatsorban (itt a listában).
"""

"""
lista =[12, 5, 4, 8, 9, 11, 10, 15, 6]

min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam

print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)
"""


lista =[12, 5, 3, 8, 9, 11, 10, 16, 6]

def maximum(list):
    max1 = list[0]
    for szam in list:
        if szam > max1:
            max1 =szam
    return max1

print(f'A lista legnagyobb eleme: {maximum(lista)}')


lista =[12, 5, 3, 8, 9, 11, 10, 16, 6]

def minimum(list):
    min1 = list[0]
    for szam in list:
        if szam < min1:
            min1 =szam
    return min1

print(f'A lista legkisebb eleme: {minimum(lista)}')


lista3 =[12, 5, 2, 8, 9, 11, 10, 16, 6]
print(f'{maximum(lista) - minimum(lista3)}')

lista5 =[12, 5, 2, 8, 9, 11, 10, 16, 6]
def osszeg(lista):
    ossz = 0
    for szam in list:
        ossz = ossz + szam
    return ossz
print(f'A lista5 lista elemeinek összege: {osszeg(lista5)}')