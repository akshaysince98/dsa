from math import sqrt

n = int(input("Enter an integer: "))


def printFactorsBrute(n):
    num = n
    result = []
    for i in range(1, n+1):
        if num % i == 0:
            result.append(i)

    return result


def printFactorsBetter(n):
    num = n
    result = []
    for i in range(1, (n//2)+1):
        if num % i == 0:
            result.append(i)

    result.append(n)

    return result


def printFactorsBest(n):
    num = n
    result = []
    for i in range(1, int(sqrt(n))+1):
        if num % i == 0:
            result.append(i)
            result.append(n//i)

    # result.sort()
    return result


print("Brute Factors of given number are: ", printFactorsBrute(n))
print("Better Factors of given number are: ", printFactorsBetter(n))
print("Best Factors of given number are: ", printFactorsBest(n))
