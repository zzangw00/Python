N = int(input())
count = 0
n = N
while True:
    a = n // 10
    b = n % 10
    sum = a + b
    sum_b = sum % 10
    n = int(str(b) + str(sum_b))
    count += 1
    if n == N:
        print(count)
        break


