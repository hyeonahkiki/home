import sys
sys.stdin = open('input.txt', 'r')


# 미로를 탐색할 함수를 설정
def maze():
    # 이동하는 좌표들을 넣을 스택을 생성
    stack = []
    # 시작점을 기준으로 사방을 봐서 갈 수 있는 곳을 찾아야되기에
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    # 시작좌표를 넣고 시작한다.
    stack.append([startI, startJ])
    # 스택이 차있다는 것은 갈 수 있는 좌표들을 넣어놨다는 것
    while len(stack) != 0:
        # 좌표를 꺼낸다.
        spot = stack.pop()
        i = spot[0]
        j = spot[1]
        # 지나간 길을 표시하기 위해 roads자체를 바꿈. 1로표시
        roads[i][j] = 1
        # 시작점에서 4방향 중 갈 수 있는 좌표를 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 새로운 좌표가 미로안에 있고
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                # 0이면 갈 수 있는 곳. stack에 넣기
                if roads[ni][nj] == 0:
                    stack.append([ni, nj])
                # 3이면 도착지점으로 끝
                elif roads[ni][nj] == 3:
                    return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    roads = [list(map(int, input())) for x in range(N)]
    for i in range(N):
        for j in range(N):
            # 2가 출발점. 그래서 2의 좌표를 시작점으로 잡음
            # startI, statJ가 시작좌표
            if roads[i][j] == 2:
                startI = i
                startJ = j

    print('#{} {}'.format(tc, maze()))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def maze():
    q = []
    q.append([startI, startJ])
    while q:
        spot = q.pop(0)
        i = spot[0]
        j = spot[1]
        roads[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if roads[ni][nj] == 0:
                    q.append([ni, nj])
                elif roads[ni][nj] == 3:
                    return 1
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
