import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #글자판크기, 회문의 길이
    words_horizon = [list(input()) for x in range(N)]
    words_veritcal = list(zip(*words_horizon))
    words= words_horizon + words_veritcal
    for word in words:
        for i in range(N-M+1):
            temp = word[i:i+M:1]
            if temp == temp[::-1]:
                print('#{} {}'.format(tc, ''.join(temp)))