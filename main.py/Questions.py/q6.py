"Take two number as input. print the greater of the two. if they are equal ,print both are equl"

num1 = int(input("Enter the number ="))
num2 = int(input("Enter the number ="))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is than {num1}")
else:
    print("both are equal")
