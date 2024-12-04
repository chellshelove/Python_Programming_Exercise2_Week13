def myfibonacci_memo(n, memo={}):
    # Base cases
    if n == 0 or n == 1:
        return 1
    # Check if already computed
    if n not in memo:
        memo[n] = myfibonacci_memo(n - 1, memo) + myfibonacci_memo(n - 2, memo)
    return memo[n]

# Example usage
n = 5
print(f"The {n}th Fibonacci number is: {myfibonacci_memo(n)}")