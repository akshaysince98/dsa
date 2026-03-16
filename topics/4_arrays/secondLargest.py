nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def secondLargest(nums):

    largest = float("-inf")
    secLarge = float("-inf")

    for n in nums:
        if n > largest:
            secLarge = largest
            largest = n
        elif n > secLarge and n != largest:
            secLarge = n

    return secLarge


print("The second largest element in array is: ", secondLargest(nums))
