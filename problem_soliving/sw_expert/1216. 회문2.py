import sys

sys.stdin = open('input.txt', 'r')

for i in range(1, 2):
    tc = int(input())
    # 가로
    board = [list(input()) for x in range(100)]
    # 세로
    board2 = list(zip(*board))
    # 전체
    total = board + board2
    # 회문의 최대 길이
    maxV = 0
    for word in total:
        # 범위 설정
        for i in range(len(word)):
            # 회문체크, 길이체크
            check = ''
            length = 0
            for k in range(i, 100):
                check += word[k]
                if check[::] == check[::-1]:
                    length = len(check)
                if maxV < length:
                    maxV = length
    print('#{} {}'.format(tc, maxV))
