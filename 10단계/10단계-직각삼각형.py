while True:
    arr = list(map(int, input().split()))
    a = max(arr)
    if sum(arr) == 0:
        break
    arr.remove(a)
    if arr[0] ** 2 + arr[1] ** 2 == a ** 2:
        print("right")
    else:
        print("wrong")