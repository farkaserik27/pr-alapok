szam = int(input("Adj meg egy számot! "))
szam1 = int(input("Adj meg egy másik számot! "))
if szam > szam1:
    print("A nagyobb érték: {szam1}")
elif szam < szam1:
    print("A nagyobb érték: {szam}")
else:
    print("A két szám egyenlő")