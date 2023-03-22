print()
print("Schaltjahrprüfer")
print("================")
print()
year = int(input("Gib das Jahr ein: "))
print()
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "ist ein Schaltjahr.")
        else:
            print(year, "ist kein Schaltjahr.")
    else:
        print(year, "ist ein Schaltjahr.")
else:
    print(year, "ist kein Schaltjahr.")
print()
print("Programmende.")
print()