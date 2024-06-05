keresztnev= input("Adja meg a keresztnevét: ")
kor = int("Adja meg az életkorát: ")

if kor <= 1:
    print("A kora alapján", {keresztnev}, "csecsemő!")
elif kor < 6:
    print("A kora alapján", {keresztnev}, "kisgyerek!")
elif kor < 12:
    print("A kora alapján", {keresztnev}, "gyerek!")
elif kor < 16:
    print("A kora alapján", {keresztnev}, "serdülő!")
elif kor < 25:
    print("A kora alapján", {keresztnev}, "ifjú!")
elif kor < 65:
    print("A kora alapján", {keresztnev}, "felnőtt!")
