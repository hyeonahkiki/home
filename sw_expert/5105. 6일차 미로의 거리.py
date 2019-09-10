import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def maze():
    global roads
    # 방문을 표시하고 거리를 계산하려면 필요
    visited = [[0] * N for x in range(N)]
    q = []
    q.append([startI, startJ])
    while q:
        spot = q.pop(0)
        i = spot[0]
        j = spot[1]
        # 방문한 곳 표시
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if roads[ni][nj] == 0:
                    visited[ni][nj] =1
                #먼가.....있을거같은데
                    q.append([ni, nj])
                # 3도 1로 표시해서 출발점, 도착점 1씩해서 2 빼면 될거같은데
                # 그러면 00000 있는 곳도 똑같아 지는거같은데..ㅇㅅㅇ...
                # 그냥 3을 만났을 때만 계산해서 리턴?
                if roads[ni][nj] ==3:
                    visited[ni][nj] =1
                return visited[][] -2
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    roads = [list(map(int, input())) for x in range(N)]
    for i in range(N):
        for j in range(N):
            if roads[i][j] == 2:
                startI = i
                startJ = j
    print('#{} {}'.format(tc, maze()))

    #새로만든 배열에 1씩 증가시켜가서 해보는 걸로

