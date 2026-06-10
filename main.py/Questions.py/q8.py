"Take a year as input. check if is aleap year. a year is a leap year if it is divided by 4,but not by 100, unless it is also divisible by 400"

year = int(input("Enter a year="))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print("its is not a leap yaer ")
