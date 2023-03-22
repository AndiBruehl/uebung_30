print() #Leerzeile zur besseren Lesbarkeit
file = input("Textdatei angeben: ") #Einlesen der Textdatei
with open(file, "r") as f:  #öffnen der Textdatei
    for line in f:  #for-Schleife
        print() #Leerzeile zur besseren Lesbarkeit
        print(line.strip().swapcase()) #Ändern der Groß- und Kleinschreibung und Ausgabe im Terminal
        print() #Leerzeile zur besseren Lesbarkeit