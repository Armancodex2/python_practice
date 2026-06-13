"print all the number which are divisible by 3 and 5 , from 1 to 100"

count = 1

while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print(count)
    count += 1
