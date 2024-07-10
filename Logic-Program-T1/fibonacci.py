def fibonacci(n):
    fib_series = []
    if n <= 0:
        return fib_series
    elif n == 1:
        fib_series.append(0)
        return fib_series
    else:
        fib_series = [0, 1]
        while len(fib_series)<n:
            fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series


num_terms = int(input("Enter integer number"))
fib_series = fibonacci(num_terms)
print(f"The Fibonacci series with {num_terms} terms is: {fib_series}")
