"""
# eljárás - program

def koszont_nevvel(nev):
    print('Szia '+ nev +', üdv a fedélzeten!')

koszont_nevvel('Ádám')

print("---------------------------------------")
"""

"""
#függvény - érték
def koszont_nevvel2(vezetéknév, keresztnév):
    print (f'Szia {vezetéknév} {keresztnév}, üdv a fedélzeten!')

koszont_nevvel2('Farkas , Erik')

print("---------------------------------------")
"""

#fügvény - érték
def koszont_nevvel1(nev1):
    uzenet = 'Szia '+ nev1 +',üdv a fedélzeten!'
    return uzenet

print(koszont_nevvel1('Ádám1'))

print('---------------------------------------')