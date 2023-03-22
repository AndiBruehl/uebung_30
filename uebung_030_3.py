def search_list(list, element):
    if element in list:
        return True
    else:
        return False

my_list = input("Gib eine Liste von Elementen durch Kommas und Leerzeichen getrennt ein: ").split(", ")
print()
search_element = input("Gib das zu suchende Element ein: ")
print()
print(search_list(my_list, search_element))