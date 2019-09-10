import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 뿔의 수, 동물의 수
    N, M = map(int, input().split())
    # 연립방정식으로 풀기
    for i in range(M + 1):
        uni_cnt = i
        twin_cnt = M - i
        if twin_cnt * 2 + uni_cnt == N:
            break
    print('#{} {} {}'.format(tc, uni_cnt, twin_cnt))
