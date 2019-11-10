import sys
sys.stdin = open('input', 'r')

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

def check(i, j, b):
    global land, visited, N, M
    front = -1
    rear = -1
    q = [0] * N *M
    rear += 1
    q[rear] = [i, j]
    visited[i][j] = b
    while front != rear:
        front +=1
        x, y = q[front]
        for k in range(8):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni< M and 0<=nj<N and visited[ni][nj] ==0:
                if land[ni][nj] ==1:
                    visited[ni][nj] = b
                    rear += 1
                    q[rear] = [ni, nj]
    return

# 1은 땅, 0은 바다
# 세로, 가로
while 1:
    N, M = map(int, input().split())
    if N ==0 and M == 0:
        break
    else:
        # 배열
        land = [list(map(int, input().split())) for x in range(M)]
        visited = [[0]*N for _ in range(M)]

        k = 0
        for i in range(M):
            for j in range(N):
                if land[i][j] ==1 and visited[i][j] ==0:
                    k += 1
                    check(i, j, k)
        print(k)
