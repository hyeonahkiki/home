import sys
sys.stdin = open('input', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(i, j, n):
    home_cnt = 0
    q = []
    visited[i][j] = 1
    q.append([i, j])
    while q:
        x, y = q.pop(0)
        # 방문한 칸 수를 세기 위해
        home_cnt += 1
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni<n and 0<=nj<n and visited[ni][nj] ==0:
                if space[ni][nj] == 1:
                    visited[ni][nj] = 1
                    q.append([ni, nj])
    return home_cnt


N = int(input())
space = [list(map(int, input())) for x in range(N)]
visited = [[0] * N for x in range(N)]
cnt = 0
home = []
for i in range(N):
    for j in range(N):
        if space[i][j] ==1 and visited[i][j] ==0:
            cnt += 1
            home.append(bfs(i, j, N))
print(cnt)
for i in home:
    print(i)