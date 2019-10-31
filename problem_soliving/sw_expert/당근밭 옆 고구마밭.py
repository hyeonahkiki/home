import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 구역의 개수
    N = int(input())
    sweets =list(map(int, input().split()))+[0]
    # 줄기의 수
    cnt = 0
    # 줄기의 길이
    length = 1
    max_length =0
    # 줄기의 개수는 오른쪽이 자신보다 작아지는 순간 +1
    #줄기의 고구마수
    maxV = 0
    temp = 0

    for i in range(1, N):
        if sweets[i-1] < sweets[i]:
            length += 1
        else:
            if length >=2:
                cnt += 1
                if length > max_length:
                    max_length = length
                    temp = sum(sweets[i-max_length:i])
                    maxV = temp
                    length= 1
                    temp = 0
                elif length == max_length:
                    temp = max(sum(sweets[i-max_length:i]), sum(sweets[i-length:i]))
                    maxV = temp
                    length = 0
                else:
                    cnt += 1
    if i ==N-1:
        if length >= 2:
            cnt += 1
            if length > max_length:
                max_length = length
                temp = sum(sweets[i+1 - max_length:i+1])
                maxV = temp
            elif length == max_length:
                temp = max(sum(sweets[i - max_length:i]), sum(sweets[i - length:i]))
                maxV = temp
                print(sweets[i-max_length-1:i-max_length+1], sweets[i+1 - length:i+1])
    print('#{} {} {}'. format(tc, cnt, maxV))