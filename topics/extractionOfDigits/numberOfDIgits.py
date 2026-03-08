from math import *

n = int(input("Enter a number: "))


def countDigits(n):
    num = n
    digits = 0
    while num > 0:
        digits += 1
        num = num//10

    return digits


def countDigitsUsingLog(n):
    return int(log10(n))+1


print("number of digits in n:", countDigits(n))
print("number of digits in n using log:", countDigitsUsingLog(n))
