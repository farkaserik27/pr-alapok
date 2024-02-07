import random

magassagok = [random.randint(0, 9) for _ in range(31)]
print("Magasságok:", magassagok)

meredek_elore = 0
for i in range(1, len(magassagok)):
    if magassagok[i] >= magassagok[i-1] + 2:
        meredek_elore += 1

meredek_vissza = 0
for i in range(len(magassagok)-2, -1, -1):
    if magassagok[i] >= magassagok[i+1] + 2:
        meredek_vissza += 1

print("Előre haladva meredek szakaszok száma:", meredek_elore)
print("Visszafelé haladva meredek szakaszok száma:", meredek_vissza)