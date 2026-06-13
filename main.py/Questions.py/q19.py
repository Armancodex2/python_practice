# ask a number from the user , and print all the factor.

num = int(input("Enter the number= "))

i = 1

while i <= num:
    if num % i == 0:
        print(i)
        i += 1
