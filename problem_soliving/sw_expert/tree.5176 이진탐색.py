import sys

sys.stdin = open('input.txt', 'r')

"""
왼쪽 > 위로 올라가고 > 오른쪽 탐색 ==> 중위순회
"""


# 시작점, 마지막 도착 노드 설정
def inorder(n, last):
    # 노드의 유효성 먼저 확인
    global  cnt
    while n <= last:
        inorder(n * 2, last)  # 왼쪽노드부터 탐색
        tree[n] = cnt
        cnt += 1
        inorder(n*2+1, last) # 오른쪽 노드부터 탐색
        return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 기록할 트리를 만들어준다
    tree = [0] * (N + 1)
    cnt = 1
    inorder(1, N)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
