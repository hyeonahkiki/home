import sys
sys.stdin = open('input', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def check():
    global maze, visited, N, M
    q=[0] * N *M
    front = -1
    rear = -1
    rear += 1
    q[rear] = [1, 1]
    visited[1][1] = 1
    while front != rear:
        front += 1
        spot = q[front]
        i = spot[0]
        j = spot[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 1<= ni< N+1 and 1<=nj<M+1:
                if maze[ni][nj] == 1 and visited[ni][nj]==0:
                    rear += 1
                    q[rear] = [ni, nj]
                    visited[ni][nj] = visited[i][j] + 1
    return visited[N][M]



N, M = map(int, input().split())
maze = [[0]* (M+1)]+[[0]+list(map(int, input())) for x in range(N)]
visited = [[0]*(M+1) for x in range(N+1)]
print(check())
