import sys
sys.stdin = open('input.txt', 'r')

# 받은 카드를 검증하는 함수
def winner(lists):
    check = [0] * 10
    for i in lists:
        check[i] += 1
    # triplet 체크
    for j in check:
        if j >= 3:
            return True
    # run 체크
    for j in range(len(check) - 2):
        if check[j] >= 1 and check[j + 1] >= 1 and check[j + 2] >= 1:
            return True
    return False

# 승자를 검증하는 함수
def game(cards):
    p1 = []
    p2 = []
    for i in range(len(cards)):
        if not i % 2:
            p1.append(cards[i])
            # 카드를 받고 나서 바로 검사
            # 바로 검증할 함수가 필요
            if winner(p1):
                return 1
        else:
            p2.append(cards[i])
            # 카드를 받고나서 바로검사
            # 바로 검증할 함수가 필요
            if winner(p2):
                return 2
    # 무승부일때 처리
    else:
        return 0

T = int(input())
# p1, p2가 카드를 받고 시작하면 안된다.
# 받아서 run이나 triplet이 나오면 바로 게임을 종료해야되기 때문에
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, game(cards)))
