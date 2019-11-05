import sys

sys.stdin = open('input.txt', 'r')

# 최대값좌표 주변 4방향을 탐색하며 살펴볼 함수가 필요
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def check():
    global q, road, visited, N
    length = 1
    while q:
        spot = q.pop(0)
        i = spot[0]
        j = spot[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[i][j] == 0:
                if road[i][j] > road[ni][nj]:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1
                    length += 1
    return length


T = int(input())
for tc in range(1, T + 1):
    # 지도 크기, 최대 공사 가능 깊이
    N, K = map(int, input().split())
    road = [list(map(int, input().split())) for x in range(N)]
    visited = [[0] * N for x in range(N)]
    # road안에서 최대값을 구한다
    maxV = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] > maxV:
                maxV = road[i][j]

    # 최대값 좌표들을 담을 것이 필요
    q = []
    for i in range(N):
        for j in range(N):
            if road[i][j] == maxV:
                q.append([i, j])
                visited[i][j] = 1
    print(check())
