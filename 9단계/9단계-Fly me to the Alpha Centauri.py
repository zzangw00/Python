t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    a = y - x
    num = 1
    while True:
        if num ** 2 <= a < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == a:
        print((num * 2) - 1)
    elif num ** 2 < a <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)