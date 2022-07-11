name = "Tomek"

print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())

print(name[-3:])

channel = "Jak nauczyć się programowania"
print(channel.split(" "))

join_string = "-"
print(join_string.join(['Jak', 'nauczyć', 'się', 'programowania']))

print(name.startswith("T"))
print(name.startswith("t"))

print(name.endswith("k"))

print(name.rstrip("k"))
print(name.lstrip("T"))

print(name.strip())


first_name = "Tomek"
last_name = "Frydlewicz"

print(first_name + " " + last_name)

join_string = " "
print(join_string.join([first_name, last_name]))


james_bond = 7
print(str(james_bond).zfill(3))