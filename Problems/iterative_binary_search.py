#iterative method
def binary_search(arr, l, u , key):

    while (l <= u):
        mid = (l + u) // 2
        print(mid)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            l = mid + 1
        elif arr[mid] > key:
            u = mid - 1
    return  -1


arra = [1,2,3,4,5,7,9,11111]
nm = len(arra) -1

kk = binary_search(arra, 0, len(arra)-1, 9)
if kk == -1:
    print("not found")
else:
    print("its founf at",kk)
