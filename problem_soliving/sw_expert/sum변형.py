import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for x in range(100)]
    minS= 100000
    high = 100000
    for h in range(1, 30):
        right = 0
        left = 0
        minV = 100000
        for i in range(100):
            right += abs(board[i][i]-h)
            left += abs(board[i][99-i]-h)
            row = 0
            col = 0
            for j in range(100):
                row += abs(board[i][j]-h)
                col += abs(board[j][i] -h)
            if minV > row:
                minV = row
            if minV > col:
                minV = col
        if minV> right:
            minV =right
        if minV > left:
            minV = left
        if minS > minV:
            minS = minV
            high= h
    print('#{} {} {}'.format(tc, minS, high))