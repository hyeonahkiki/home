import sys
sys.stdin = open('input.txt', 'r')

# t : 이전까지의 합
def check(n, k, t):
    global minV
    if n ==k:
        if minV > t:
            minV = t
        return minV
    if t > minV:
        return
    else:
        for i in range(N):
            if used[i] != 1:
                res[n] = factory[n][i]
                used[i] = 1
                check(n+1, k, t+res[n])
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for x in range(N)]
    res = [0] * N
    used = [0] * N
    result = []
    minV = 1000000
    check(0, N, 0)
    print('#{} {}'.format(tc, minV))