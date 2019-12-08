import sys
sys.stdin = open('input', 'r')

def check(n, k, s, t):
    if n==s:
        for j in range(s):
            print(res[j], end=' ')
        print()
    else:
        for i in range(t, k+1):
            if used[i] != 1:
                res[n] = i
                used[i] = 1
                check(n+1, k, s, t+1)
                used[i] = 0


N, M = map(int, input().split())
used = [0] * (N+1)
res = [0] * M
check(0, N, M, 1)
