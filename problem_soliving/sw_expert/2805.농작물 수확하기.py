import sys
sys.stdin = open('input.txt', 'r')

T= int(input())
N = int(input())
farm = [list(map(int, input())) for x in range(N)]
profit = 0

for x in range(N):
    for y in range(N):
        if N//2<= x+y <= 2*(N-1) - N//2:
            if abs(x-y) <=N//2:
                profit += farm[x][y]
print(profit)