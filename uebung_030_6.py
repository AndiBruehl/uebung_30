progfunction = input("Funktioniert das System? [JA/NEIN] ")

if progfunction == "JA":
    print("Fummel nicht daran herum! Alles ist gut.")
else:
    guilty = input("Bist du Schuld? [JA/NEIN] ")
    if guilty == "NEIN":
        print("Dich trifft es nicht!")
    else:
        print("Du bist ein Idiot!")
        recog = input("Hat es jemand gemerkt? [JA/NEIN] ")
        if recog == "NEIN":
            print("Man wird dich nie finden!")
        else:
            print("Du bist am Arsch!")
            guilt2 = input("Kannst du jemand anderem die Schuld zuschieben? [JA/NEIN] ")
            if guilt2 == "NEIN":
                print("Du bist wirklich am Arsch!")
            else:
                print("Keine Sorge, jemand anderes ist am Arsch!")