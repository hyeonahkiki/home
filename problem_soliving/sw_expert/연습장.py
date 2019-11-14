import sys
sys.stdin = open('input.txt', 'r')

# 미네랄 인덱스, 미네랄개수, 누적미네랄양, 에너지
def check(n, k, s, e):
    global maxV, mineral, dis, robot, N, M
    if maxV < s:
        maxV = s
    if n==k:
        return
    else:
        # 그거를 가지고 돌아올때는 에너지가 0이어도 상관이 없으니까
        if e >= 2*dis[n]:
            # 미네랄을 가져올때
            # 왕복 거리를 뺴야하니까
            check(n+1, k, s+mineral[n][2], e-2*dis[n])
        # 미네랄을 가져오지 않을때
        # 에너지가 얼마가 있던지 상관이 없음
        check(n+1, k, s, e)

T = int(input())
for tc in range(1, T+1):
    #가로, 세로, 에너지
    N, M, C = map(int, input().split())
    field = [list(map(int, input().split())) for x in range(N)]
    # 최대 미네랄 양
    maxV = 0
    # 로봇의 위치를 찾기
    robot = []
    # 미네랄의 양
    mineral = []
    # 미네랄별 거리정보
    dis = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                robot.append([i, j])
            elif field[i][j] > 1:
                mineral.append([i, j, field[i][j]])
    for m in mineral:
        x, y, z = m
        temp = abs(robot[0][0] - x) + abs(robot[0][1] - y)
        dis.append(temp)
    check(0, len(mineral), 0, C)
    print(dis)