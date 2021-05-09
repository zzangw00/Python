import sys
n = int(sys.stdin.readline())
arr = []
sum = 0
for i in range(n):
    arr.append(int(sys.stdin.readline()))
    sum += arr[i]

print(sum - n + 1)