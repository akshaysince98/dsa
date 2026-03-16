n = int(input("Enter a number: "))


def checkPalindrom(n):
    num = n
    reverse = 0
    while num > 0:
        reverse = (reverse * 10) + num % 10
        num = num // 10

    return reverse == n


print(f"is {n} a palindrome? {checkPalindrom(n)}")
