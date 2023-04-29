def nth_fibonacci(n):
    return n if n <= 1 else nth_fibonacci(n-1) + nth_fibonacci(n-2)


n = int(input("Enter n: "))
print(nth_fibonacci(n))
