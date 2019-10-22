import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = [list(map(int, input().split())) for x in range(N)]
    res = []

    s1 = 0
    for i in range(N//2):
        for j in range(i+1, N-1-i):
            s1 += carrots[i][j]
    res.append(s1)

    s2 = 0
    for i in range(1, N-1):
        if i <= N//2:
            for j in range(N-i, N):
                s2 += carrots[i][j]
        else:
            for k in range(i+1, N):
                s2 += carrots[i][k]
    res.append(s2)

    s3 = 0
    for i in range(N//2+1, N):
        for j in range(N-i, i):
            s3 += carrots[i][j]
    res.append(s3)

    s4 = 0
    for i in range(1, N-1):
        if i <= N//2:
            for j in range(0, i):
                 s4 += carrots[i][j]
        else:
            for k in range(0, N-i-1):
                s4 += carrots[i][k]
    res.append(s4)

    total = max(res) - min(res)
    print('#{} {}'.format(tc, total))