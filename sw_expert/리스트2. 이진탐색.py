import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 전체, a가 찾을거, b가 찾을거
    P, A, B = map(int, input().split())
    # 각각 몇번 했는지 세기
    cnt_a = 0
    cnt_b = 0
    # 이진탐색 이용
    left = 0
    right = P
    middle = P//2
