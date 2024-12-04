def myfibonacci_iterative(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = 5
print(f"The {n}th Fibonacci number is: {myfibonacci_iterative(n)}")