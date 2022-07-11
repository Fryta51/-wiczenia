names_list = []
names_list.append("Tomek")
names_list.append("Michał")

names_list = ["Tomek", "Michał", "Mariusz", "Tomek"]

names_list2 = ["Kacper"]

names_list3 = names_list + names_list2
print(names_list3)

names_list.reverse()

print(names_list)

names_list.sort()
names_list.sort(reverse=True)
print(names_list)

for name in names_list:
    print(name)

print(names_list[0])

print(names_list.count("Tomek"))

print(len(names_list))

names_list.remove("Tomek")
print(names_list)

names_list.clear


person = ("Tomek", "Frydlewicz", 21)

print(person)
print(person.count("Tomek"))


names_set = {"Tomek", "Michał", "Tomek"}

print(names_set)

names_set = set()
names_set.add("Tomek")
names_set.add("Łukasz")

names_set.remove("Łukasz")
names_set.discard("Łukasz")

print(names_set)

for name in names_set:
    print(name)

names_set2 = {"Miłosz", "Kacper"}

names_set3 = names_set.union(names_set2)
for name in names_set3:
    print(name)


names_set.update(names_set2)
for name in names_set:
    print(name)


names_set3 = names_set.difference(names_set2)
names_set3 = names_set.intersection(names_set2)
for name in names_set3:
    print(name)

names_list = ["Artur", "Rafał"]

names_list.extend(names_set2)
print(names_list)


countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin"}
countries_and_capitals['Czechia'] = "Prague"

print(countries_and_capitals)
for country, capital in countries_and_capitals.items():
    print(country + "-" + capital)

print(countries_and_capitals["Poland"])
print(countries_and_capitals.get("Poland"))

print(countries_and_capitals.setdefault("USA", "Washington DC"))

if "Poland" in countries_and_capitals.keys():
    print("Znaleziono")
else:
    print("Nie znaleziono")