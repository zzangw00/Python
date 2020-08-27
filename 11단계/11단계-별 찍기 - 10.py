a = int(input())

star = []
for _ in range(a):
    star.append(["*" for _ in range(a)])

divide = a
cnt = 0
while divide != 1:
    divide /= 3
    cnt += 1

for n in range(cnt):

    idx = [i for i in range(a) if (i // 3 ** n) % 3 == 1]
    for i in idx:
        for j in idx:
            star[i][j] = " "

for _ in star:
    print("".join(_))