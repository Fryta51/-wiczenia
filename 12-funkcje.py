countries_information = {}
countries_information["Polska"] = ("Warszawa", 32.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

def show_country_info(country):
    country_information = countries_information.get(country)

    print()
    print(country)
    print("------")
    print("Stolica: " + country_information[0])
    print("Liczba mieszkańców (mln): " + str(country_information[1]))

for country in countries_information.keys():
    print(country)

country = input("informacje o jakim kraju chcesz wyświetlić? ")
show_country_info(country)


def display_sum(a, b):
    print(a+b)

display_sum(2, 3)

def calculate_sum(a, b):
    return a + b

calculate_sum(2, 3)

def print_message():
    print("To jest super wiadomość")

print_message()