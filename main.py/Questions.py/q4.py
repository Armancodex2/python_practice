"A student scored marks in 3 subjects. take all thre as three as input , calculate the total and average, and print both using an f-string."

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subjct2:"))
marks3 = int(input("Enter marks for subject3:"))

total = marks1 + marks2 + marks3
average = total / 3

print(f"total = {total}")
print(f"average ={average}")
