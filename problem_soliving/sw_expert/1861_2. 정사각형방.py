import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for x in range(N)]
    v = [0] * ((N * N)+1)
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if room[i][j] + 1 == room[ni][nj]:
                        v[room[i][j]] = 1

    cnt = 0
    num = N*N+1
    maxV = 0
    # 시작점
    for j in range(len(v)):
        # 움직이는 점
        for i in range(len(v)):
            if v[j+i] ==1:
                cnt += 1
            else:
                if maxV < cnt:
                    maxV = cnt
                    num = j
                cnt = 0
                break
    print('#{} {} {}'.format(tc, num, maxV+1))
