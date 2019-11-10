import sys
sys.stdin = open('input', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# i, j 위치정보, 집단별로 찍을 값
def check(i, j, b):
    global farm, M, N,visited

    front = -1
    rear = -1
    q = [0] * M * N
    rear += 1
    q[rear] = [i, j]
    while front != rear:
        front += 1
        x, y = q[front]
        visited[x][y] = b
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni < M and 0<=nj < N and visited[ni][nj]==0:
                if farm[ni][nj] ==1:
                    visited[ni][nj] = b
                    rear += 1
                    q[rear] = [ni, nj]

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

    visited = [[0] * N for x in range(M)]
    k = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and visited[i][j]==0:
                k += 1
                check(i, j, k)
    print(k)
