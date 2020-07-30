n = int(input())
for i in range(n):
    cnt = 0
    evg = 0
    sum = 0
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)):
        sum += arr[j]
    evg = sum / arr[0]
    for j in range(1, len(arr)):
        if arr[j] > evg:
            cnt += 1
    print('%.03f' % float(cnt / (len(arr) - 1) * 100) + "%")