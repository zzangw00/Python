n = int(input())
a = int(input())
arr = list(map(int, str(a)))
sum = 0
for i in range(len(arr)):
    sum += arr[i]

print(sum)

