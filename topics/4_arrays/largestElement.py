nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def largestElement(nums):

    largest = nums[0]

    for n in nums:
        if n > largest:
            largest = n

    return largest


print("The largest element in array is: ", largestElement(nums))
