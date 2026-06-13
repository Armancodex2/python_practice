# Take number as  input from the user one by one skip negative number adn keep adding the positive ones . stop when the user enter 0 and print the total.(uses both continue and break.)


total = 0

while True:
    num = int(input("Enter a number: "))

    if num < 0:
        continue

    if num == 0:
        break

    total += num

print("Total =", total)
