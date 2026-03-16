nums = list(map(int, input("Enter the array: ").split()))
# [1,1,1,2,3,4,4,7,9]


def numberOfUniqueElementsBruteForce(nums):
    freq = {}

    for n in nums:
        freq[n] = 0

    i = 0
    for f in freq:
        nums[i] = f
        i += 1

    return i


print("Number of unique elements in array are:",
      numberOfUniqueElementsBruteForce(nums))
