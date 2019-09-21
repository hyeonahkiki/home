# 사용한 원소, 사용할 수 있는 원소 수
import sys
sys.stdin = open('input.txt', 'r')


def f(n, k):
    if n == k:
        print(res)
        result.append(sum(res))
        return
    else:
        for i in range(k):
            if used[i] != 1:
                res[n] = boards[n][i]
                # res[n] = boards[i]
                used[i] = 1
                f(n + 1, k)
                used[i] = 0
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    boards = [list(map(int, input().split())) for x in range(N)]
    #
    res = [0] * N
    # 사용한 거 표시
    used = [0] * N
    print(boards)
    result = []
    f(0, N)
    print(min(result))

