import sys

sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def check(x, y):
    global maze
    stack = []
    stack.append([x, y])
    maze[x][y] = 1
    while stack:
        spot = stack.pop()
        i = spot[0]
        j = spot[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<16 and 0<=nj<16:
                if maze[ni][nj] == 0:
                    maze[ni][nj] = 1
                    stack.append([ni, nj])
                if maze[ni][nj] ==3:
                    return 1
    return 0



for tc in range(1, 16):
    tc_N = int(input())
    maze = [list(map(int, input())) for x in range(16)]
    startI = 0
    startJ = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                startI = i
                startJ = j
    print('#{} {}'.format(tc, check(startI, startJ)))
