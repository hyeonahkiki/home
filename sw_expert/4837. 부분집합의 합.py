import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 원소의 수, 부분집합의 합
    N, K = map(int, input().split())
    # 집합 a생성
    a = []
    for i in range(1, 13):
        a.append(i)
    # 부분집합 모을 리스트 생성
    subset = []
    # 부분집합 생성하기
    # 부분집합의 개수
    for i in range(1<<N):
        # 원소의 수만큼 비트를 비교함
        for j in range(N):
            # i의 j번째 비트가 1이면 j번째 원소 출력
            if i & (1<<j):
                print(a[j], end=',')
        print()
