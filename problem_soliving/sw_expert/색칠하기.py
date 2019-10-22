import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * 10 for x in range(10)]
    for s in range(N):
        r1, c1, r2, c2, check = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += check
    ans = 0
    for x in range(10):
        ans += board[x].count(3)
    print('#{} {}'.format(tc, ans))
