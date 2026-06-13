# ask the number form the user, print the multiplication table upto 10.

num = int(input("Enter the number= "))
i = 1

while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1
