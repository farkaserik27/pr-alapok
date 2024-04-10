import random



class Kor:
    def __init__(self, sugar, kozepont=(0, 0)):
        self.sugar = sugar
        self.kozepont = kozepont

    def terulet(self):
        return self.sugar * pow(3.14, 2)

    def kerulet(self):
        return self.sugar *3.14 * 2
    
'''
kor01 = Kor(5)
print(kor01.kozepont())

kor02 = Kor(10, (1, 1))
print(kor02.kozepont)
'''

'''
A korok nevű listában tárol 5 darab kor obejktumot, melyek surgara
[0; 10] tartományba eső, véletlenszersűen előállított számérték.
'''

korok = []
for _ in range(5):
    kor = Kor(random.randint(1, 10))
    korok.append(kor)

for kor in korok:
    print(kor.sugar, kor.kerulet)

print(korok[1].sugar)