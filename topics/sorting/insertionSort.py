nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def insertionSort(arr):

    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


insertionSort(nums)

print("The sorted array is: ", nums)
