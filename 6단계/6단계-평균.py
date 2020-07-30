n = int(input())
arr = list(map(int, input().split()))
result = 0
max = max(arr)
for i in range(len(arr)):
    result += arr[i] / max * 100

print(result / n)