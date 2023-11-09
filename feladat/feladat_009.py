#feladat_009
"""
Kérjünk be két egész számot, szám1 és szám2
Hasonlítsuk össze a két számot, és irassuk ki, hogy a szám1 kisebb mint
szám2, vagy a szám2 kisebb mint a szám1, vagy a szám1 egyenlő szám2-vel.
"""

szam1=input("Kérek egy számot /szam1/: ")
szam2=input("Kérek egy másik számot /szam2/: ")
szam1=int(szam1)
szam2=int(szam2)

"""
if szam1 < szam2:
    print(f"A szam1 kisebb, mint szam2")
elif szam2 < szam1:
    print(f"A szam2 kisebb, mint  szam1")
else:
    print(f"A szam1 egyenlő a szam2")
"""

"""
if szam1 < szam2:
    print(f"A szam1 kisebb, mint szam2")
if szam2 < szam1:
    print(f"A szam2 kisebb, mint  szam1")
if sza1 == szam2:
    print(f"A szam1 egyenlő a szam2")
"""

if szam1 < szam2:
    print(f"A szam1 kisebb, mint szam2")
elif szam2 < szam1:
    print(f"A szam2 kisebb, mint  szam1")
elif szam1 == szam2:
    print(f"A szam1 egyenlő a szam2")