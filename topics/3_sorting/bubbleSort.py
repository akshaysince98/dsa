nums = list(map(int, input("Enter the array: ").split()))
# [2, 3, 4, 1, 5]


def bubbleSort(arr):

    for i in range(len(arr)):

        is_unsorted = False

        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_unsorted = True

        if is_unsorted == False:
            print("Array is sorted, breaking")
            break

    return arr


print("The sorted array is: ", bubbleSort(nums))
