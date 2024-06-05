homerseklet = int(input("Írd be a hőmérsékletedet: "))
if homerseklet < 37:
    print("Normális a hőmérsékletedet")
elif homerseklet >= 40:
    print("Menny el a korházba")
elif homerseklet >= 38:
    print("Lázas vagy")
elif homerseklet >= 37:
    print("Hőemelkedésed van")