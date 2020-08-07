n = int(input())
first = 1
step = 6
cnt = 1
if n == 1:
    print(first)

else:
    while n > first:
        cnt += 1
        first += step
        step += 6
    print(cnt)