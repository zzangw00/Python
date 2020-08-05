arr = list(map(int, input().split()))
if arr[2] <= arr[1]:
    print(-1)
else:
    print((arr[0] // (arr[2] - arr[1])) + 1)