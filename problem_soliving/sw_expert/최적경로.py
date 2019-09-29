import sys
sys.stdin = open('input.txt', 'r')

def distance(x, y):
    global spot
    x1 = spot[x][0]
    y1 = spot[x][1]
    x2 = spot[y][0]
    y2= spot[y][1]
    d = abs(x1-x2) + abs(y1-y2)
    return d
def check(n, k):
    global minV
    if n==k:
        total = 0
        for i in range(k-1):
            total += distance(res[i]+2, res[i+1]+2)
        total += distance(0, res[0]+2)
        total += distance(1, res[-1]+2)
        if minV > total:
            minV = total
        return
    else:
        for i in range(k):
            if used[i] != 1:
                res[n] = i
                used[i] = 1
                check(n+1, k)
                used[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pre = list(map(int, input().split()))
    spot = []
    for i in range(0, len(pre)-1, 2):
        spot.append([pre[i], pre[i+1]])
    res = [0] * N
    used = [0] * N
    minV = 100000
    check(0, N)
    print('#{} {}'.format(tc, minV))