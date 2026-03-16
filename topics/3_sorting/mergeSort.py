nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def merge_arrays(left, right):
    result = []

    i = 0
    j = 0

    left_len = len(left)
    right_len = len(right)

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # if i < left_len:
    #     while i < left_len:
    #         result.append(left[i])
    #         i += 1

    # if j < right_len:
    #     while j < right_len:
    #         result.append(right[j])
    #         j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_part = arr[:mid]
    right_part = arr[mid:]

    left = mergeSort(left_part)
    right = mergeSort(right_part)

    return merge_arrays(left, right)


print("The sorted array is: ", mergeSort(nums))
