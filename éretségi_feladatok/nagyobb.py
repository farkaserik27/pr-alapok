szam = int(input("Adj meg egy számot! "))
szam1 = int(input("Adj meg egy másik számot! "))
if szam > szam1:
    print(f"A nagyobb érték: {szam}")
elif szam < szam1:
    print(f"A nagyobb érték: {szam1}")
else:
    print("A két szám egyenlő")