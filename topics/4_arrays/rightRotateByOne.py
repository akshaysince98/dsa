nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def rightRotateByOne(nums):
    l = len(nums)
    temp = nums[l-1]
    for i in range(l-2, -1, -1):
        nums[i+1] = nums[i]

    nums[0] = temp
    return nums


print("The rotated by one array is: ", rightRotateByOne(nums))
