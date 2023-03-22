import datetime
import time

# Datum der Osterferien in diesem Jahr (2023)
osterferien = datetime.datetime(2023, 4, 11, 00, 00, 00)

while True:
    # Aktuelles Datum und Zeit
    jetzt = datetime.datetime.now()

    # Berechne die verbleibende Zeit bis zu den Osterferien
    verbleibende_zeit = osterferien - jetzt

    # Wenn es bereits Ostern ist, beende das Programm
    if verbleibende_zeit.days < 0:
        break

    # Berechne die verbleibende Zeit in Stunden, Minuten und Sekunden
    stunden, reste = divmod(verbleibende_zeit.seconds, 3600)
    minuten, sekunden = divmod(reste, 60)

    # Gib den Countdown aus
    print(f"Verbleibende Zeit bis zu den Osterferien: {verbleibende_zeit.days} Tage, {stunden:02d}:{minuten:02d}:{sekunden:02d}")

    # Warte eine Sekunde, bevor die nächste Zeile ausgegeben wird
    time.sleep(1)


print("\nFrohe Ostern!")
print()
