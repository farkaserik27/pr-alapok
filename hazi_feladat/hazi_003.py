from random import randrange
randomSzam = randrange(1, 5)
print("Adj meg egy számot! ")
bemenet = int(input)

if bemenet == randomSzam:
    print("A két szám egyezik.")
elif bemenet > randomSzam:
    print("A szám nagyobb, mint a random szám.")
else:
    print("A szám kisebb, mint a random szám.")