#recursive
n = int(input("number"))
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Generate the first 10 numbers in the Fibonacci sequence
fib_sequence = [fibonacci(i) for i in range(n)]
print(fib_sequence)


