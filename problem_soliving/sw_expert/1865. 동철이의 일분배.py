import sys
sys.stdin = open('input.txt', 'r')

def check(n, k, s):
    global maxV
    if s <= maxV:
        return
    if n == k:
        if maxV < s:
            maxV = s
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                # res[n] = i
                check(n+1, k, s *(pct[n][i]/100))
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pct = [list(map(int, input().split())) for x in range(N)]
    res = [0] * N
    used = [0] * N
    maxV = 0
    check(0, N, 1)
    maxV *= 100
    maxV = '%.6f' % maxV
    print('#{} {}'.format(tc, maxV))