N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = list()
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                sum.append(arr[i] + arr[j] + arr[k])

print(max(sum))