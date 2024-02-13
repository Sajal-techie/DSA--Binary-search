arr = [9,8,8,7,6,5,4,3,3,3,3,2,1]

low = len(arr) - 1
high = 0
key = 13
while high <= low:
    mid = (high + low)//2
    if arr[mid] == key:
        print(mid)
        break
    elif arr[mid] < key:
        low = mid - 1
    else:
        high = mid + 1
else:
    print("not found")