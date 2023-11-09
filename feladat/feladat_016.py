#feladat_016.py
#While ciklus III.
folytatja = True
while folytatja:
    print(f'Vidd ki a szemetet!')
    valasz = input(f'Mondjam még egyszer? (i/n): ')
    if valasz == 'n':
        folytatja = False
print(f'Program vége!')
