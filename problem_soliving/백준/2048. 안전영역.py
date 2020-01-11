import sys
sys.stdin = open('input', 'r')

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, rain):
    q = [[i, j]]
    visited[i][j] = 1
    while q:
        i, j = q.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni< N and 0<=nj<N and visited[ni][nj] == 0:
                if space[ni][nj] > rain:
                    visited[ni][nj] = 1
                    q.append([ni, nj])


N = int(input())
space = [list(map(int, input().split())) for x in range(N)]
maxV = -1

for rain in range(0, 101):
    visited = [[0] * N for x in range(N)]
    # 안전영역 개수 세기
    safe = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] > rain and visited[i][j] ==0:
                dfs(i, j, rain)
                safe += 1
    if maxV < safe:
        maxV = safe
print(maxV)
