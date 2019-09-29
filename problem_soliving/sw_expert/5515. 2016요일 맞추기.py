import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 월, 일
    m, d = map(int, input().split())
    # 금, 토, 일, 월, 화, 수, 목(1월 1일이 금요일이라)
    week = [4, 5, 6, 0, 1, 2]
    #인덱스를 맞추기 위해 0을 넣음
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 날짜를 합한 다음에 요일을 계산하기 위해서
    ans = (sum(days[:m])+d) % 7
    print('#{} {}'.format(tc,week[ans-1]))


