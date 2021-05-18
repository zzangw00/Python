n, m = map(int, input().split())

check = [False] * (n + 1)
a = [0] * m

def solution(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()

        return
    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        a[index] = i
        solution(index + 1, n, m)
        check[i] = False

solution(0, n, m)