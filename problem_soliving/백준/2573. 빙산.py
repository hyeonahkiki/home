import sys

sys.stdin = open('input', 'r')

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(i, j):
    q = [[i, j]]
    # 빙산인데 녹여서 바다가 되는 경우를 체크하기 위해서
    visited = [[0] * M for x in range(N)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        check[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if iceberg[ni][nj] == 0:
                    iceberg[i][j] -= 1
                    if iceberg[i][j] < 0:
                        iceberg[i][j] = 0
                elif iceberg[ni][nj] != 0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for x in range(N)]

time = 0

while 1:
    cnt = 0
    # 탐색을 여러번 반복하지 않기 위해서
    check = [[0]*M for x in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if iceberg[i][j] != 0 and check[i][j] == 0:
                bfs(i, j)
                cnt += 1

    # 빙산이 2개 이상이 되는 순간 끝
    if cnt > 1:
        break
    # 빙산이 2개로 분리되지 않고 녹아버리는 경우
    if cnt == 0:
        time = 0
        break
    time += 1
print(time)


