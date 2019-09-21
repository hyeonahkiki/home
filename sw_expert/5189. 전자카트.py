import sys

sys.stdin = open('input.txt', 'r')
def check(n, k):
    if n ==k-1:
        print(res)
        total = 0
        for i in range(k):
            total += golf[res[i]][res[i+1]]
        return
    else:
        for i in range(1, k):
            if used[i] != 1:
                res[n+1] = i
                used[i] = 1
                check(n+1, k)
                used[i] = 0
    return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    golf = [list(map(int, input().split())) for x in range(N)]
    # res = [1] + [0] *(N-1) +[1]
    res = [0] * (N+1)
    used = [0] * (N+1)
    result = []
    # 함수
    check(0, N)
    print('#{} {}'.format(tc, result))