#       0  1  2  3   4   5   6   7   8  9  10
nums = [5, 7, 4, 64, 32, 17, 53, 85, 3, 1, 999]

n = len(nums)
# i = 0
# count = 0
# while i <= n - 1:
#     if nums[i] % 2 == 0:
#         count += 1
#     i += 1

# print(count)
i = n - 1
while i >= 0:
    print(nums[i], end=" ")
    i -= 1
