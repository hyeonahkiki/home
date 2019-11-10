import sys
sys.stdin = open('input.txt', 'r')

spotI = {
    1: [-1, 0, 1, 0],
    2: [-1, 1],
    3: [0, 0],
    4: [-1, 0],
    5: [1, 0],
    6: [1, 0],
    7: [-1, 0]
}

spotJ = {
    1: [0, 1, 0, -1],
    2: [0, 0],
    3: [-1, 1],
    4: [0, 1],
    5: [0, 1],
    6: [0, -1],
    7: [0, -1]
}

# 각 통료별 이동할 수 있는 통로 정리하기
move = {
    1: [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]],
    2: [[1, 2, 5, 6], [1, 2, 4, 7]],
    3: [[1, 3, 4, 5], [1, 3, 6, 7]],
    4: [[1, 2, 5, 6], [1, 3, 6, 7]],
    5: [[1, 2, 4, 7], [1, 3, 6, 7]],
    6: [[1, 2, 4, 7], [1, 3, 4, 5]],
    7: [[1, 2, 5, 6], [1, 3, 4, 5]]
}


def check(r, c):
    global N, M, visited, tunnel, spotI, spotJ, L, move
    q = [0] * N * M
    front = rear = -1
    rear += 1
    # 좌표랑 시간카운트할값을 같이 넣어줌
    q[rear] = [r, c, 0]
    visited[R][C] = 1
    while front != rear:
        front += 1
        i, j, cnt = q[front]
        # 멘홀 위치에 따른 지하터널 번호를 알아내기
        if cnt == L - 1:
            break
        else:
            # for num in range(1, 8):
            #     if tunnel[i][j] == num:
            # 있어도 문제는 없는데 필요없음

            tunnel_value = tunnel[i][j]  # 지금 위치의 파이프 값을 구해주고서
            di = spotI[tunnel_value]  # 그값들 이용
            dj = spotJ[tunnel_value]  # 여기도 이용
            for k in range(len(di)):  # 여기서 k는 현아가 정의해놓은 지금 위치의 파이프에서 가능한 방향들의 인덱스.
                ni = i + di[k]
                nj = j + dj[k]

                # 각 방향으로 이동해서, 범위안이고, 방문안했고, 0이아니면,
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and tunnel[ni][nj] != 0:
                    # for x in range(len(di)):
                    # 만약 현재가 1번 파이프이고, 위에서 k(방향)이 정해져서, 그 방향에 가능한 move[tunnel_value][k]만 봐야하는데,
                    # 이렇게 for문을 돌면 range(4)이고 x = 0, 1, 2, 3 모두 돌게되고,
                    # tunnel[ni][nj] 가 move[tunnel_value][0] , move[tunnel_value][1], move[tunnel_value][2], move[tunnel_value][3] 모두를 보게된다.
                    # 맞지 않는 파이프까지 가능하도록 만들어서 오답.

                    # 그러니까 한방향만 확인하면 된다.
                    # 지금 현재 이동한 방향의 인덱스는 k이고, 그 방향에 가능한 값들은 move[tunnel_value][k] 이다.
                    if tunnel[ni][nj] in move[tunnel_value][k]:  # 가능한 방향인가 ?
                        visited[ni][nj] = 1
                        rear += 1
                        q[rear] = [ni, nj, cnt + 1]
    return


T = int(input())
for tc in range(1, T + 1):
    # 지하터널 세로, 가로/ 맨홀위치 가로, 세로 / 소요시간
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for x in range(N)]
    visited = [[0] * M for x in range(N)]

    check(R, C)
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                ans += 1
    print('#{} {}'.format(tc, ans))
