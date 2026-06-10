"Take the user's age as input. Check and print whether they are eligible to vote (age >= 18) and whether they are a senior citizen (age >= 60)."

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

if age >= 60:
    print("Senior citizen")
else:
    print("Not a senior citizen")
