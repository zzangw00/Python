arr = list(map(str, input().split()))
arr_s = list()
arr_n = list()
for i in range(len(arr)):
    arr_s.append(list(arr[i]))
    arr_s[i].reverse()
    arr_s[i] = int("".join(arr_s[i]))
if arr_s[0] > arr_s[1]:
    print(arr_s[0])
else:
    print(arr_s[1])