n = input()
arr = list(n)
arr.sort(reverse=True)
a = int(''.join(arr))
if '0' not in arr:
    print(-1)
else:
    if a % 3 != 0:
        print(-1)
    else:
        print(a)