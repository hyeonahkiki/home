import sys

sys.stdin = open('input.txt', 'r')


# 나눠가진 리스트 두개를 넣는다.
def shuffle(first, second):
    global i, ans
    while i < N // 2:
        ans.append(first[i])
        ans.append(second[i])
        i += 1
    return


T = int(input())
for tc in range(1, T + 1):
    # 카드의 수
    N = int(input())
    card = list(input().split())
    # N이 홀짝일때 나눠갖는 카드가 달라지기 때문에
    # 범위를 설정할 변수를 설정
    check = N // 2
    if N % 2:
        check += 1
    first = [card[i] for i in range(0, check)]
    second = [card[i] for i in range(check, N)]
    ans = []
    # 나눠가진 카드의 길이가 같을때
    # 움직일 좌표를 설정
    i = 0
    if len(first) == len(second):
        shuffle(first, second)
    else:
        shuffle(first, second)
        ans.append(first[i])
    print('#{} {}'.format(tc, ' '.join(ans)))
