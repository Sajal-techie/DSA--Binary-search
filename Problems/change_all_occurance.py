arr = [6,6,10,10,10,10,22]
low = 0
high = len(arr) - 1
x = 10
new = 11
while low <= high:
    mid = (low + high)//2
    if arr[mid] == x:
        left, right = mid,mid
        while left > 0 and arr[left - 1] == x :
            left = left - 1
            print(left,'left')
        while right < len(arr) - 1 and arr[right + 1] == x:
            right = right + 1
            print(right,'right')
        for i in range(left, right + 1):
            arr[i] = new
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("not found yet")
print(arr)