def solution(s):
    arr = list(map(str, str(s)))
    a = "abcdefghijklmnopqrstuvwxyz"
    arr_s = list(map(str, str(a)))
    arr_n = []
    for i in range(len(arr_s)):
        if arr_s[i] in arr:
            for j in range(len(arr)):
                if arr_s[i] == arr[j]:
                    arr_n.append(j)
                    break
        elif arr_s[i] not in arr:
            arr_n.append(-1)
    for i in range(len(arr_n)):
        print(arr_n[i], end=' ')
if __name__ == '__main__':
    s = str(input())
    solution(s)