n = int(input())
a = 0
arr = list(map(int, input().split()))

for i in arr:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        a += 1
print(a)