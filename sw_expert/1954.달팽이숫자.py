di = [0, 1, 0, -1] #방향쓰는거 중요 매우 중요!!
dj = [1, 0, -1, 0] #di랑 dj랑 방향이 맞아야함!!!!! 두개의 방향만 맞으면 순서는 상관없음

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    snail_move = [[0]*N for x in range(N)]
    i = 0
    j = 0
    k = 1
    dir = 0

    while k <= N * N:
        snail_move[i][j] = k
        k += 1
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni>=0 and ni<N and nj>=0 and nj<N and snail_move[ni][nj] ==0:
            i, j = ni, nj
        else:
            dir = (dir+1) % 4
            i += di[dir]
            j += dj[dir]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(snail_move[i][j], end=' ')
        print()