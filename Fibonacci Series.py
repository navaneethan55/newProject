def fibonacci(N):
    a, b = 0, 1
    for _ in range(N):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
fibonacci(8)
