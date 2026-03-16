nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def partition(arr, low, high):
    i, j = low, high
    pivot = arr[low]

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quickSort(arr, low, high):

    if low < high:
        pivot_idx = partition(arr, low, high)

        quickSort(arr, low, pivot_idx-1)
        quickSort(arr, pivot_idx+1, high)

    return arr


print("The sorted array is: ", quickSort(nums, 0, len(nums)-1))
