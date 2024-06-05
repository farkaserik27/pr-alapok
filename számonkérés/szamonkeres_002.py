#Farkas Erik 10/D
"""
Bekérek egy egész számot irasuk ki hogy a szám negatív, pozitiv vagy nula
"""
egesz_szam = int(input("Kérek egy egész számot. "))
if egesz_szam < 0:
    print("A szám negatív.")
elif egesz_szam > 0:
    print("A szám pozitív.")
else