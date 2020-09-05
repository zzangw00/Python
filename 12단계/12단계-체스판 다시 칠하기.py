def solution(n, m):
    arr = []
    arr2 = []
    result = []
    for i in range(n):
        arr.append(str(input()))
    for i in range(n):
        line = []
        for j in arr[i]:
            line.append(j)
        arr2.append(line)

    for i in range(n - 7):
        for j in range(m - 7):
            count1 = 0
            count2 = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if k % 2 == 0 and l % 2 == 0:
                        if arr2[k][l] != 'W':
                            count1 += 1
                    elif k % 2 == 0 and l % 2 == 1:
                        if arr2[k][l] != 'B':
                            count1 += 1
                    elif k % 2 == 1 and l % 2 == 0:
                        if arr2[k][l] != 'B':
                            count1 += 1
                    elif k % 2 == 1 and l % 2 == 1:
                        if arr2[k][l] != 'W':
                            count1 += 1

            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if k % 2 == 0 and l % 2 == 0:
                        if arr2[k][l] != 'B':
                            count2 += 1
                    elif k % 2 == 0 and l % 2 == 1:
                        if arr2[k][l] != 'W':
                            count2 += 1
                    elif k % 2 == 1 and l % 2 == 0:
                        if arr2[k][l] != 'W':
                            count2 += 1
                    elif k % 2 == 1 and l % 2 == 1:
                        if arr2[k][l] != 'B':
                            count2 += 1

            result.append(min(count1, count2))

    print(min(result))

if __name__ == '__main__':
    n, m = map(int, input().split())
    solution(n, m)