import sys
sys.stdin = open('input.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def make(n, i, j, w):
    if n == 6:
        nums.add(w)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<4 and 0<=nj<4:
                make(n+1, ni, nj, w+board[ni][nj])



T = int(input())
for tc in range(1, T+1):
    board = [list(input().split()) for x in range(4)]
    nums = set()
    for i in range(4):
        for j in range(4):
            make(0, i,j, board[i][j])
    print("#{} {}".format(tc, len(nums)))