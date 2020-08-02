def solution(n):
    for i in range(n):
        arr_s = []
        arr = list(map(str, input().split()))
        arr_n = list(map(str, arr[1]))
        for j in range(len(arr_n)):
            for k in range(int(arr[0])):
                arr_s.append(arr_n[j])
        print("".join(arr_s))
if __name__ == '__main__':
    n = int(input())
    solution(n)