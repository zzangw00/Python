def solution(num):
    if(num <= 1):
        return False
    i = 2
    while i * i <= num:
        if(num % i == 0):
            return False
        i += 1
    return True

num_list = [x for x in range(1, 123456 * 2 + 1)]
for i in num_list:
    if(solution(i)):
        num_list[i - 1] = 1

while(True):
    num = int(input())
    if(num == 1):
        print(num)
        continue
    if(num == 0):
        break
    cnt = 0    
    for i in range(num + 1, 2 * num + 1):
        if(num_list[i - 1] == 1):
            cnt += 1
    print(cnt)