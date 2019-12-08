import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 최소 힙
    heap = [0] * (N+1)
    # 힙에 넣어줄때마다 cnt를 세야한다.
    cnt = 0
    for num in nums:
        heap[cnt+1] = num
        cnt += 1
        # 넣어줄때마다 비교하면서 바꿔줘야한다.
        # idx를 확인해서 제일 작은 값을 올려야 한다.
        idx = cnt
        while heap[idx] < heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx //= 2
    res = 0
    # 마지막 노드의 조상노드에 저장된 정수의 합 구하기
    # len(heap)과 cnt가 다른경우가 존재한다.
    # len(heap)를 마지막 인덱스로 잡으면 cnt와 달라져서 답이 틀릴 가능성이 생긴다
    # 그리고 문제에서는 우선순위큐를 구현하기 위해 힙을 이용해서 넣고 빼고를 하기 때문에
    # 애초에 len(heap)으로 접근할 수 없다.
    # 매우 주의!!!!!!!!!!!!!!!!! cnt로 조상노드를 찾아가야함!!!!!!!!!!!!!!!!!!
    while cnt != 0:
        res += heap[cnt//2]
        cnt //= 2
    print('#{} {}'.format(tc, res))
