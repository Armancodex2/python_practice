# sum of all the number from 1 to 100 divisible by 2 and 7


start = int(input("Enter the start number= "))
end = int(input("Enter the end number= "))

i = 1
total = 0

while i <= 100:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i += 1

print("Total =", total)
