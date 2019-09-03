T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input())) for x in range(N)]

    for i in range(N):
        s = 0
        s += square[0][N//2]
        s += square[N-1][N//2]
        for j in range(N):
            if j == N //2:
                s += square[i][j]
        # for a in range(i+1, N-1):
        #     if 0 < j < N //2:
        #         s += square[a][j]
    print('#{} {}'.format(tc, s))


