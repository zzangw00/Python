N = int(input())

for i in range(1, N + 1):
    for j in range(i):
        print("*", end="")
    print()
for i in range(N + 1, 2 * N):
    for j in range(i - (2 * (i - N))):
        print("*", end="")
    print()