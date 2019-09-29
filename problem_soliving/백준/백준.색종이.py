import sys
sys.stdin=open('input.txt', 'r')

N = int(input())
spot = [list(map(int, input().split())) for x in range(N)]
drawing = [[0]* 101 for x in range(101)]
for i in spot:
    x = i[0]
    y = i[1]
    for k in range(x, x+10):
        for s in range(y, y+10):
            drawing[k][s] = 1
    cnt = 0
    for i in drawing:
        cnt += i.count(1)
print(cnt)
