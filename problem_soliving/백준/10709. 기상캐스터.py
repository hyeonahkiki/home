import sys

sys.stdin = open('input', 'r')
# 가로, 세로
H, W = map(int, input().split())
cloud = [list(input()) for x in range(H)]
# 이동하는 거 체크
check = [[-1] * W for x in range(H)]
# 위치 넣기
q =[]
for i in range(H):
    for j in range(W):
        if cloud[i][j] == 'c':
            check[i][j] = 0
            q.append([i, j])

while q:
    spot=q.pop(0)
    x = spot[0]
    y = spot[1]
    nj = y + 1
    if 0 <= x < H and 0 <= nj < W:
        if cloud[x][nj] != 'c' and check[x][nj] == -1:
            check[x][nj] = check[x][y] + 1
            q.append([x, nj])
for i in range(H):
    for j in range(W):
        print(check[i][j], end=' ')
    print()
