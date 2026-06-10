"Take a number as input . without *,calculate and print their product using += in a way that adds the first number to itself the second number of times.(think carefully)"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = 0

for i in range(num2):
    product += num1

print("Product =", product)
