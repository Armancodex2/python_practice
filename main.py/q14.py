"A shop give discount based on purchase amount."

"above 5000 - 20% discount"
"above 3000 - 10% discount "
"above 1000 - 5% discount"
"below 1000 - no discount"

amount = float(input("Enter purchase amount: "))

if amount > 5000:
    discount = 20
elif amount > 3000:
    discount = 10
elif amount > 1000:
    discount = 5
else:
    discount = 0

print("Discount =", discount, "%")
