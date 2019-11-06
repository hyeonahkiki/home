import sys
sys.stdin = open('input', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def check():
    global farm, M, N
    q = [0] * M * N
    front = -1
    rear = -1
    visited = [[0]*N for x in range(M)]

    for i in range(M):
        for j in range(N):
            if farm[i][j] ==1:
                rear += 1
                q[rear] = [i, j]
    front += 1
    spot= q[front]
    x = spot[0]
    y = spot[1]
    visited[x][y] = 1
    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0<=ni < M and 0<=nj < N and visited[ni][nj] ==0:
            visited[ni][nj] = visited[i][j] + 1
    return




T = int(input())
for tc in range(1, T+1):
    # 가로밭의 길이, 세로길이, 위치의 개수
    M, N, K = map(int, input().split())
    # 배추밭
    farm = [[0]*N for x in range(M)]
    for k in range(K):
        i, j = map(int, input().split())
        farm[i][j] = 1
    check()