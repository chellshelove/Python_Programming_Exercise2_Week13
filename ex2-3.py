import numpy as np

def myfibonacci_matrix(n):
    if n == 0:
        return 1
    F = np.array([[1, 1], [1, 0]])
    result = np.linalg.matrix_power(F, n - 1)
    return result[0][0] + result[0][1]

# Example usage
n = 5
print(f"The {n}th Fibonacci number is: {myfibonacci_matrix(n)}")