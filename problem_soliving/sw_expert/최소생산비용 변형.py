import sys
sys.stdin = open('input.txt', 'r')

def check(n, k):
    global minV
    if n==k:
        distance = 0
        for i in range(k):
            distance += abs(local[i][0]-factory[i][0]) + abs(local[i][1] - factory[i][1])
        if minV > distance:
            minV = distance
        return
    else:
        for i in range(k):
            if used[i] != 1:
                res[n] = i
                used[i] = 1
                check(n+1, k)
                used[i] = 0


N = int(input())
local = [list(map(int, input().split())) for x in range(N)]
factory = [list(map(int, input().split())) for x in range(N)]
res = [0] * N
used = [0] * N
minV = 100000
check(0, N)
print(minV)