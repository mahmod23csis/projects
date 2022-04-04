empDict = {}

id_in = input("Enter ID or -999 to quit: ")
while id_in != '-999':
    name = input("Enter a name: ")
    empDict[id_in] = name
    id_in = input("Enter ID or -999 to quit: ")

name = input("Enter a name to find or -999 to quit: ")
while name != '-999':
    found = False
    for key, value in empDict.items():
        if name == value:
            print(name, "has key", key)
            found = True
    if found == False:
        print("Name not found")
    name = input("Enter a name to find or -999 to quit: ")

id_in = input("Enter an ID to delete or -999 to quit: ")
while id_in != '-999': 
    if id_in in empDict:
        del empDict[id_in]
        print(id_in, "has been removed.")
    else:
        print("No delete – ID not found")
    id_in = input("Enter an ID to delete or -999 to quit: ")

id_in = input("Enter ID to change its name or -999 to quit: ")
while id_in != '-999':
    if id_in in empDict:
        new_name = input("Enter a new name: ")
        empDict[id_in] = new_name
    else:
        print("ID not found")
    id_in = input("Enter ID to change its name or -999 to quit: ")

print("ID\t Name")
for key in empDict:
    print(key,"\t", empDict[key])
