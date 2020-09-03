def solution(n):
    arr = []
    lank = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    for i in range(len(arr)):
        count = 1
        for j in range(len(arr)):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                count += 1
        lank.append(count)

    for i in lank:
        print(i, end=" ")

if __name__ == '__main__':
    n = int(input())
    solution(n)