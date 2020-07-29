N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end='')
    for j in range((2 * N - 1) - (2 * i)):
        print("*", end='')
    print()

for i in range(N + 1, 2 * N):
    for j in range(i - (2 * (i - N)) - 1):
        print(" ", end='')
    for j in range((i - N) * 2 + 1):
        print("*", end='')
    print()