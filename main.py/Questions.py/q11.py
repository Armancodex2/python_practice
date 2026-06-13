"Take a person's age and whether  they have a valid ID (ture/false) as input . they can enter venue only if they are 18 or older AND have a valid ID. print the appropriate message."

age = int(input("Enter age: "))
valid_id = input("Do you have a valid ID? (True/False): ") == "True"

if age >= 18 and valid_id:
    print("You can enter the venue.")
else:
    print("You cannot enter the venue.")
