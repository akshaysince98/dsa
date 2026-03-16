n = int(input("Enter a number: "))


def findFactorial(n):
    if n == 0 or n == 1:
        return 1

    return n * findFactorial(n-1)


print(f"the factorial of {n} is : {findFactorial(n)}")
