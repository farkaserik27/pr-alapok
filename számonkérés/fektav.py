#Farkas Erik 10/D

vezeto = input(int('Kérem, adja meg hány éves: '))
if vezeto < 18:
    print(f'Nem használható életkor!')
elif vezeto > 24:
    print(f'A reakcióidő 1 másodperc.')
elif vezeto > 34:
    print(f'A reakcióidő 0,8 másodperc.')
elif vezeto > 44:
    print(f'A reakcióidő 0,6 másodperc.')
elif vezeto > 54:
    print(f'A reakcióidő 0,5 másodperc.')
elif vezeto > 60:
    print(f'A reakcióidő 0,7 másodperc.')
else:
    print(f'A reakcióidő 1 másodperc és egyre lassulnak.')