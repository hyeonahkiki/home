import sys

sys.stdin = open('input.txt', 'r')


def cnt(a, b, c, d):
    sums=0
    for x in range(a, b):
        for y in range(c, d):
            sums += carrot[x][y]
    return sums


T = int(input())
for tc in range(1, T + 1):
    # 가로, 세로
    N, M = map(int, input().split())
    carrot = [list(map(int, input().split())) for x in range(N)]
    minV = 1000000
    for i in range(N - 1):
        for j in range(M - 1):
            s1 = cnt(0, i+1, 0, j+1)
            s2 = cnt(0, i+1, j + 1, M)
            s3 = cnt(i + 1, N, 0, M)
            res = (max(abs(s1-s2), abs(s2-s3), abs(s3-s1)))
            if minV > res:
                minV = res
    print(f'#{tc} {minV}')

