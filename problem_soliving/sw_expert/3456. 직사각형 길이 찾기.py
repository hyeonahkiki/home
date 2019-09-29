import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    length = list(map(int, input().split()))
    # 원소를 넣은 후 개수가 모자란 변을 출력/같으면 길이가 3
    check = []
    ans = 0
    for i in range(3):
        check.append(length[i])
        if check.count(length[i]) == 3:
            ans = length[i]
    for i in range(3):
        if check.count(length[i]) == 1:
            ans = length[i]
    print('#{} {}'.format(tc, ans))

