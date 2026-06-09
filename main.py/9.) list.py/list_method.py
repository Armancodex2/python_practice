lst = ["Anirudh", 54, 21.98, True, "Surat", 54, 54]

print(lst, id(lst))
# lst.append(100)
# lst.append("Delhi")
# lst.insert(2, "Delhi")
# lst.insert(0, "Muskan")

# lst.pop()
# lst.pop(0)  # By index

lst.remove(543)
print(lst, id(lst))


nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

# Sort vs Sorted
# new_list = sorted(nums)
# print(f"new_list = {new_list}", id(new_list))

print(f"nums = {nums}", id(nums))
nums.sort(reverse=True)  # In place sorting
print(f"nums = {nums}", id(nums))
