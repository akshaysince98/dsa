n = int(input("Enter an integer: "))


def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


print(f"The {n}th item in fibonacci series is: {fib(n)}")
