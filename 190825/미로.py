#sw-expert stack1-미로
def maze(i, j, s):
    global N
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    q= []
    s[i][j] = 1
    q.append([i, j])

    while len(q) != 0:
        t = q.pop()
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if ni >=0 and ni < N and nj>=0 and nj<N :
                if s[ni][nj] == '3':
                    return 1
                elif s[ni][nj] == '0':
                    s[ni][nj] =1
                    q.append([ni, nj])
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    roads = [list(map(int, input())) for x in range(N)]
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if roads[i][j] ==2:
                startI = i
                startJ = j
                print(maze(i, j, roads))

    print('#{} {}'.format(tc, maze(startI, startJ, roads)))


