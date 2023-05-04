import math

def minOperations(n):
    if n < 1:
        return 0
    result = 0
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n = n // i
                count += 1
            result += count
        i += 1
    if n > 1:
        result += 1
    return result
