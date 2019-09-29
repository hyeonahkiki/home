import sys
sys.stdin = open('input', 'r')

# 한층의 창문 개수, 층수
N, M = map(int, input().split())
window = [list(input()) for x in range(5*N+1)]
check = [0] * 5

