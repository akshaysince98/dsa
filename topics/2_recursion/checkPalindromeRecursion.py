
s = input("Enter a string: ")

left = 0
right = len(s)-1


def checkPalindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return checkPalindrome(s, left+1, right-1)


print(f"Is {s} a palindrome? {checkPalindrome(s, left, right)}")
