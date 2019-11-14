import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 봉우리 좌표, 등산로 길이, 깎을 수 있는 기회
def check(i, j, road, cut):
    global maps, N, visited, maxL, K
    visited[i][j] =1
    if maxL < road:
        maxL = road
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] ==0:
            if maps[i][j] > maps[ni][nj]:
                check(ni, nj, road+1, cut)
            else:
                # 기회가 있을때만 깎을 수 있음!!!!!!
                if cut != 0:
                    origin = maps[ni][nj]
                    if maps[ni][nj]-K < maps[i][j]:
                        maps[ni][nj] = maps[i][j] -1
                        check(ni, nj, road+1, 0)
                        maps[ni][nj] = origin
    visited[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    # 지도 크기, 최대 공사 가능 깊이
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for x in range(N)]
    # 방문표시하기
    visited = [[0] * N for x in range(N)]
    # 제일 긴 길이
    maxL = 0
    # 최고 봉우리 찾기
    peak = 0
    for i in range(N):
        for j in range(N):
            if peak < maps[i][j]:
                peak = maps[i][j]

    # 봉우리 좌표를 바로 함수로 보내서 하기
    for i in range(N):
        for j in range(N):
            if peak == maps[i][j]:
                check(i, j, 1, 1)



    print('#{} {}'.format(tc, maxL))