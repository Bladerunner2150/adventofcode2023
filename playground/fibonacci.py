def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

n = 100
fib_sequence = fibonacci(n)
print(fib_sequence)

# series = [int((((1 + 50.5) / 2) * n - ((1 - 50.5) / 2) * n) / 5**0.5) for n in range(1, 21)]
# print(series)