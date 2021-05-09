n, m, k = map(int, input().split())
arr = []
for i in range(k + 1):
    newN = n - i
    newM = m - (k - i)
    arr.append(min(newN // 2, newM // 1))

print(max(arr))