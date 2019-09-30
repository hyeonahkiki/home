import sys

sys.stdin = open('input', 'r')

# 한층의 창문 개수, 층수
N, M = map(int, input().split())
window = [list(input()) for x in range(5 * N + 1)]
check = [0] * 5

cnt =0
for i in range(0, 5 * N + 1, 5):
    for j in range(0, 5*M+1, 5):
        if i+6 <=5*N+1 and j+6 <= 5*M +1:
            for x in range(i, i+6):
                   for y in range(j, j+6):
                        if window[x][y] =='*':
 
                            cnt += 1


