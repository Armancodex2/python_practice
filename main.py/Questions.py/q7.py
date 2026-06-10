"Take a student's marks as input . print their grade based on this scale:"

"90-100 : A"
"80-89 : B"
"70-79 : C"
"60-69 : D"
"below 40 : F"

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
elif marks < 40:
    print("Grade F")
else:
    print("Invalid grade range")
