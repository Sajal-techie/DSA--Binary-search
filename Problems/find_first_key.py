def binary(arr, low, high, key):
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [1,3,4,6,7,8,9,10]
key = 1
result = binary(arr, 0, len(arr)-1, key)
if result == -1:
    print("element not found")
else:
    print("element found at position", result)