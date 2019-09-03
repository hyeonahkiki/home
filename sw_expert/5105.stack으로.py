def maze(i, j, N):
    global roads
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    stack = []
    visited = [[0] * N for x in range(N)]
    stack.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 방문점 표시

    while len(stack) != 0:
        t = stack.pop()
        i, j = t[0], t[1]
        if roads[i][j] == '3':
            if visited[i][j] =='1':
                return 0
            else:
                return visited[i][j] -2
          # 시작점이 1로 시작했기때문에 그만큼을 더 빼야한다.
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if roads[ni][nj] != '1' and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
    # 원래꺼에서 증가를 시켜야함(거리계산을 하기 위해서랑, 같은 거리에 어떤 좌표들이 있는지
                    stack.append([ni, nj])
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    roads = [list(input()) for x in range(N)]
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if roads[i][j] == '2':
                startI = i
                startJ = j

    print('#{} {}'.format(tc, maze(startI, startJ, N)))