import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    check = [0] * 10
    for card in cards:
        check[card] += 1
    # 숫자카드
    ans = 0
    cnt = 0
    for i in range(10):
        if check[i] == max(check):
            ans = i
            cnt = check[i]

    print('#{} {} {}'.format(tc, ans, cnt))
