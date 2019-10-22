import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = 0
    for i in range(N):
        per, money = map(float, input().split())
        salary = per * money
        total += salary
    print('#{} {}'.format(tc,'%.6f' % total))