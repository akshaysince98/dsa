nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def isSorted(nums):

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False

    return True


print("Is the array sorted?", isSorted(nums))
