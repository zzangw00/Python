a, b = map(int, input().split())
n = int(input())

if a + b < 2 * n:
    print(a + b)
else:
    print((a + b) - (2 * n))