from math import *

n = int(input("Enter a number: "))


def countDigits(n):
    return int(log10(n)) + 1


def checkArmstrong(n):
    num = n
    digits = countDigits(n)
    sum = 0
    while num > 0:
        ld = num % 10
        sum = sum + ld**digits
        num = num // 10

    return sum == n


print(f"is {n} an armstrong number? {checkArmstrong(n)}")
