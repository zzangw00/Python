n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i] * (i + 1))
print(max(arr2))