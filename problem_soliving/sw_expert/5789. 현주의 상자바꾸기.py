import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 상자개수, 반복횟수
    N, Q = map(int, input().split())
    box = [0] * (N + 1)
    # 변화값
    x = 0
    for i in range(Q):
        x += 1
        L, R = map(int, input().split())
        if x != Q+1:
            for j in range(L, R+1):
                box[j] = x
        else:
            break
    ans = list(map(str, box[1:]))
    print('#{} {}'.format(tc, ' '.join(ans)))
