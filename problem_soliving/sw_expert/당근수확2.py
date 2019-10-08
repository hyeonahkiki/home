import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    carrot = [0] + list(map(int, input().split()))
    #거리를 체크
    cnt = 0
    # 이동할 좌표
    i = 0
    while i <N:
        i +=1
        cnt += 1
        if carrot[i] >= M:
            carrot[i] -=M
            cnt += i
            i=0
        else:
            if i !=N:
                carrot[i+1] += carrot[i]
                carrot[i] = 0
            else:
                cnt += i
    print(cnt)