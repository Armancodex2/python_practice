# Return True if a number is prime number return False
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    return False


print(is_prime(17))
