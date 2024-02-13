# recursive method
def binary_search(arr, l, u, key ):
    if l <= u:
        mid = (l + u) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, u, key)
        elif arr[mid] > key:
            return binary_search(arr, l, mid - 1, key)
    else:
        return -1


arr = [1, 2, 4, 5, 6, 8, 9, 99]

res = binary_search(arr, 0, len(arr)-1, 99)
if res == -1:
    print("not dound")
else:
    print("element is found at",res)
