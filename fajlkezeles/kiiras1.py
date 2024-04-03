# Fájlbaírás lehetőségei:

# Megnyitási módok
# r: olvasás
# w: írás, fájlt hoz létre
# a: a létező fájl végére hozzáfűz

with open ('kimenet.txt', 'w', encoding='utf-8') as celfajl:
    #sztringet ír a fájlba
    celfajl.write('aaalma, kkörte, eeeper')
    celfajl.write('/n')
    celfajl.write('aaaaaaaaaaaaaaaalam, kkkkkkkkkkkkkkkörte, epre')