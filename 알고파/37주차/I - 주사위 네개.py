n = int(input())
arr2 = []
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()

    if len(set(arr)) == 1:
        arr2.append(50000 + (arr[0] * 5000))
    elif len(set(arr)) == 2:
        if arr[1] == arr[2]:
            arr2.append(10000 + (arr[1] * 1000))
        elif arr[1] != arr[2]:
            arr2.append(2000 + (arr[0] * 500) + (arr[2] * 500))
    elif len(set(arr)) == 3:
        for i in range(3):
            if arr[i] == arr[i + 1]:
                arr2.append(1000 + (arr[i] * 100))
                break
    else:
        arr2.append(max(arr) * 100)

print(max(arr2))
