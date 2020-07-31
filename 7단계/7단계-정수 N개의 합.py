def solve(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]

    print(solve(a))