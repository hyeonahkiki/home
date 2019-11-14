import sys
sys.stdin = open('input.txt', 'r')

# 미네랄 인덱스, 총 미네랄 수, 미네랄 총합, 에너지
def check(n, k, s, e):
    global maxV
    if e>= 0:
        if maxV < s:
            maxV = s
    if n==k:
        return
    else:
        check(n+1, k, s+mineral[n][2], e-2*dis[n])
        check(n+1, k, s, e)




T = int(input())
for tc in range(1, T+1):
    # 가로, 세로, 에너지
    N, M, C = map(int, input().split())
    ground = [list(map(int, input().split())) for x in range(N)]
    # 로봇 위치 찾기
    robot = [0, 0]
    # 미네랄 정보
    mineral = []
    # 거리
    dis = []
    # 미네랄 최대값
    maxV = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                robot= [i, j]
            elif ground[i][j] > 1:
                mineral.append([i, j, ground[i][j]])
    for i in range(len(mineral)):
        temp = abs(robot[0]-mineral[i][0])+abs(robot[1]-mineral[i][1])
        dis.append(temp)

    check(0, len(mineral), 0, C)
    print('#{} {}'.format(tc, maxV))