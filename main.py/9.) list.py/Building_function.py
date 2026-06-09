marks = [45, 34, 54, 65, 23, 65, 76, 91]

# To get the length
n = len(marks)
print(f"Length of list = {n}")

# Max
maxi = max(marks)
print(f"Maximum marks = {maxi}")
mini = min(marks)
print(f"Minimum marks = {mini}")
total = sum(marks)
print(f"Total marks = {total}")

# To sort using sorted(), it will always return you a new list
new_list = sorted(marks, reverse=True)
print(f"new_list = {new_list}")
