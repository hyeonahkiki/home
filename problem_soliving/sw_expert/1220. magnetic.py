import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 2):
    N = int(input())
    table = [list(input().split()) for x in range(N)]
    # 세로만 점검해서 확인해보면 되기에 세로로 편성
    table = list(zip(*table))
    cnt = 0
    # 1, 2가 만나면 교착상태가 된다.
    check = '12'
    for i in table:
        ans = ''
        for s in i: # 유효한 숫자 1, 2만 넣어둠
            if s == '1':
                ans += s
            if s == '2':
                ans += s
        cnt += ans.count(check) # 유효숫자중 교착상태가 몇개인지 센다
    print('#{} {}'.format(tc, cnt))
