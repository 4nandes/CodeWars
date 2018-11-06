def namelist(names):
    if len(names) == 0:
        return ""
    if len(names) == 2:
        return names[0]['name'] + " & " + names[1]['name']
    elif len(names) == 1:
        return names[0]['name']
    else:
        return names[0]['name'] + ", " + namelist(names[1:])
    

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))