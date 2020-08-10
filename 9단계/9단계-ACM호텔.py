a = int(input())

for i in range(a):
    H, W, N = map(int, input().split())
    if N / H == int(N / H):
        last = int(N / H)
    else:
        last = int(N / H) + 1
    if N % H == 0:
        first = H * 100
    else:
        first = N % H * 100
    print(first + last)