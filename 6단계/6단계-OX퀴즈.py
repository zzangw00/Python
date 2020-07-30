n = int(input())
for j in range(n):
    sum = 0
    score = 0
    arr = list(map(str, input()))
    for i in range(len(arr)):
        if arr[i] == 'X':
            score = 0
        elif arr[i] == 'O':
            score += 1
            sum += score

    print(sum)
