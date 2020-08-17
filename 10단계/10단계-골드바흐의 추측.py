def solution(n):
    a = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n, i):
                a[j] = False
    return a


def gold(primes, n):
    index = 0
    while True:
        if primes[n // 2 - index] and primes[n // 2 + index]:
            return (n // 2 - index, n // 2 + index)
        index += 1


primes = solution(10001)
for _ in range(int(input())):
    n = int(input())
    answer = gold(primes, n)
    print(answer[0], answer[1])