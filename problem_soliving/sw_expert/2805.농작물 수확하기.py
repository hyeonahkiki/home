import sys
sys.stdin = open('input.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for x in range(N)]
    profit = 0

    # for x in range(N):
    #     for y in range(N):
    #         if N//2<= x+y <= 2*(N-1) - N//2:
    #             if abs(x-y) <=N//2:
    #                 profit += farm[x][y]
    # print(profit)

    for y in range(N):
        if 0 <= y < N//2:
            for x in range(N//2-y, N//2+y+1):
                profit += farm[y][x]
        elif y==N//2:
            for x in range(N):
                profit += farm[y][x]
        elif y>N//2:
            for x in range(y-N//2, N-(y-N//2)):
                profit += farm[y][x]
    print('#{} {}'.format(tc, profit))