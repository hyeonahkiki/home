import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N % 2:
        ans = 'Odd'
    else:
        ans = 'Even'
    print('#{} {}'.format(tc, ans))
