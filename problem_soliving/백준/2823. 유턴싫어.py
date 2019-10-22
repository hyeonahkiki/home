import sys
sys.stdin=open('input','r')
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def find():
    global R, C
    while spot:
        check = spot.pop(0)
        x = check[0]
        y = check[1]
        info[x][y] = 'X'
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0<=ni<R and 0<=nj<C:
                if info[ni][nj] =='.':
                    return 1
    return 0

#가로, 세로
R, C = map(int, input().split())
info = [list(input()) for x in range(R)]
# 위치를 저장
spot = []
for i in range(R):
    for j in range(C):
        if info[i][j] =='.':
            spot.append([i, j])
print(find())