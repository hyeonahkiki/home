import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    tc_n = int(input())
    scores = list(map(int, input().split()))
#     # 점수를 기록할 딕셔너리 생성
#     record = {}
#     for score in scores:
#         if score not in record:
#             record[score] = 1
#         else:
#             record[score] +=1
#     ans = []
#     for key, val in record.items():
#         if max(record.values()) == val:
#             ans.append(key)
#     print('#{} {}'.format(tc,max(ans)))
    cnt = [0] * 101
    for score in scores:
        cnt[score] += 1

    target_score = max(cnt)

    res = []
    for idx, val in enumerate(cnt):
        if val == target_score:
            res.append(idx)
    print('#{} {}'.format(tc, max(res)))




