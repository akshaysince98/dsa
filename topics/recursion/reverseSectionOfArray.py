arr = list(map(int, input("Enter the array elements: ").split()))
left = int(input("Enter the starting point: ") or 0)
right = int(input("Enter the ending point: ") or len(arr)-1)


def reverse(arr, left, right):

    if left >= right:
        return arr

    arr[left], arr[right] = arr[right], arr[left]

    return reverse(arr, left+1, right-1)


print("Reverse of the array is: ", reverse(arr, left, right))
