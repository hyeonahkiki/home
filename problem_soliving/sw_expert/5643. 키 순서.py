import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    # 정보모아두기
    info = []
    for x in range(M):
        a, b = map(int, input().split())
        info.append([a, b])
    # 인접행렬 만들기
    board = [[501]*(N+1) for x in range(N+1)]
    for i in range(M):
        # 작은애, 큰애
        s, h = info[i]
        board[s][h] = 1
    # 중간에 거쳐서 도달할 수 있으면 그 값으로 바꾸기
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if k!=i and i!=j and j!=k:
                    board[i][j] = min(board[i][j], board[i][k] + board[k][j])
    total = 0
    for i in range(N+1):
        rc = 0
        cc = 0
        for j in range(N+1):
            if board[i][j] != 501:
                rc += 1
            if board[j][i] != 501:
                cc += 1
        if rc + cc == N - 1:
            total += 1
    print('#{} {}'.format(tc, total))

