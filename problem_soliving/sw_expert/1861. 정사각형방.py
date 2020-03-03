import sys

sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def find(i, j):
    global pick_cnt, pick_num, res
    visited = [[0] * N for x in range(N)]
    visited[i][j] = 1
    stack = [[i, j]]
    tmp = 1
    while stack:
        x, y = stack.pop()
        first = room[x][y]
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if room[ni][nj] == first + 1:
                    visited[ni][nj] = 1
                    tmp += 1
                    stack.append([ni, nj])
    pre = tmp
    if pre > pick_cnt:
        pick_cnt = pre
        res = []
        res.append(room[i][j])
    elif pre == pick_cnt:
        res.append(room[i][j])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for x in range(N)]
    pick_num = 10000000
    res = []
    pick_cnt = 0
    for i in range(N):
        for j in range(N):
            find(i, j)
    print('#{} {} {}'.format(tc, min(res), pick_cnt))