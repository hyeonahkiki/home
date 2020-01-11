import sys
sys.stdin = open('input', 'r')

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def safe(i, j, arr):
    q = [[i, j]]
    arr[i][j] = 0
    while q:
       x, y = q.pop(0)
       for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append([ni, nj])



def bfs(i, j):
    global maxV
    start = space[i][j]
    visited = [[0] * N for x in range(N)]
    # 안전구역 개수 세기
    cnt = 0
    q = []
    q.append([i, j])
    visited[i][j] = 2
    while q:
        x, y = q.pop(0)
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] ==0:
                if space[ni][nj] < start:
                    visited[ni][nj] = 1
                    q.append([ni, nj])
                else:
                    visited[ni][nj] = 2
                    q.append([ni, nj])

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt += 1
                safe(i, j, visited)

    if cnt > maxV:
        maxV =cnt




N = int(input())
space = [list(map(int, input().split())) for x in range(N)]
maxV = -1
for i in range(N):
    for j in range(N):
        bfs(i, j)

print(maxV-1)