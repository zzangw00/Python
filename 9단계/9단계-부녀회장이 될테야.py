n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    base = [j for j in range(1, b+1)]
    for j in range(a):
        for k in range(1, b):
            base[k] += base[k - 1]
    print(base[b - 1])