cnt = 0
arr_s = list()
arr = list(map(str, input().upper()))
arr_l = list(set(arr))
for i in arr_l:
    arr_s.append(arr.count(i))
if arr_s.count(max(arr_s)) >= 2:
    print("?")
else:
    print(arr_l[arr_s.index(max(arr_s))].upper())