import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    #수강생 수, 제출한 사람 수
    N, K = map(int, input().split())
    # 제출한 사람번호
    submit = list(map(int, input().split()))
    # 0으로 찬 리스트를 만들어서 낸사람은 1로 표시
    work_cnt = [0] * (N+1)
    #제출한 사람 표시함
    not_submit = []
    for i in submit:
        work_cnt[i] = 1
    for j in range(1, len(work_cnt)):
        if work_cnt[j] == 0:
            not_submit.append(j)
    res = list(map(str, not_submit))
    print('#{} {}'.format(tc, ' '.join(res)))

