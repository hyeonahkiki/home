import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # a빵가격,b빵가격,c원
    A, B, C = map(int, input().split())
    A_cnt = C // A
    B_cnt = C // B
    if A_cnt > B_cnt:
        choice = A_cnt
    else:
        choice = B_cnt
    print('#{} {}'.format(tc, choice))
