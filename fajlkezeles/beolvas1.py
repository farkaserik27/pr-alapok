#fájl tartalmának beolvasása
# egy sor beolvasása:
with open ('otsor.txt', 'r', encoding='utf-8') as forrasfajl:
    sor = forrasfajl.readline()
    print(len(sor))
    sor = sor.strip()
    print(len(sor))
    print(sor)