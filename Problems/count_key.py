# count how many times a value is in an array

arr = [3,4,4,4,5,6,7,8,9,9,]
low = 0
high = len(arr) - 1
key = 4
count = 0
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        left, right = mid, mid
        while left >0 and arr[left - 1] == key:
            left -= 1
        while right < len(arr) - 1 and arr[right + 1] == key:
            right += 1
        for i in range(left, right + 1):
            count += 1
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
print(count)