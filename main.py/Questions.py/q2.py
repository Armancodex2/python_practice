"Take a number as input. print whether it is even or odd using the % operator and a comparison operator."

from numpy import rint

num = int(input("Enter the number ="))

if num % 2 == 0:
    print("even")
else:
    print("odd")
