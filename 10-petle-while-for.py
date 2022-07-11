number = 1

while number < 6:
    print(number)
    number += 1

for number in range(0, 20, 2):
    print(number)


for number in range(0, 10):
    if number == 5:
        break
    print(number)


for number in range(0, 10):
    if number == 5:
        continue
    print(number)