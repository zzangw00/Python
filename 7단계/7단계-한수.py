def solve(n):
    cnt = 0
    for i in range(1, n + 1):
        arr = (list(map(int, str(i))))
        if i < 100:
            cnt += 1
        elif arr[1] - arr[0] == arr[2] - arr[1]:
            cnt += 1
    print(cnt)
if __name__ == '__main__':
    n = int(input())
    solve(n)