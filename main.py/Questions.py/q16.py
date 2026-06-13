"sum of all the number from 1 to 100"

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start
total = 0

while i <= end:
    total = total + i
    i += 1

print(f"Total = {total}")
