import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int ,input().split()))
    # 최소값
    minV = 100000
    # 위치
    minI = 100000
    for i in range(N):
        # 구역별 합
        s1 = 0
        for x in range(i):
            s1 += carrot[x]
        s2 = 0
        for y in range(i, N):
            s2 += carrot[y]
        if s1 > s2:
            ans = s1-s2
        else:
            ans = s2-s1
        if minV > ans:
            minV = ans
            minI = i
    print('#{} {} {}'.format(tc, minI, minV))
