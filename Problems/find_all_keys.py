def binary_search(arr, low, high, key):
    res = []
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == key:
            left, right = mid, mid
            while left > 0 and arr[left - 1]==key:
                left -= 1
            while right < len(arr) - 1 and arr[right + 1] == key:
                right += 1
            for i in range(left,right + 1):
                res.append(i)
            return res
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1,2,3,3,3,3,3,3,4,4,4,4,4,5,6,7,8,9,10,11,12,13]
key = 3
result = binary_search(arr, 0, len(arr)-1,key )
if result == -1:
    print("element not found")
else:
    print(result)