szavak = int(input("Adj megy egy szót! "))
szavak1 = int(input("Adj meg egy másik szót! "))
if szavak > szavak1:
    print(f"A hosszabb szó: {szavak}")
elif szavak < szavak1:
    print(f"A hosszabb szó: {szavak1}")
else:
    print("A két szó egyforma hosszú: ") 