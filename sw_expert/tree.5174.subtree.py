# 전위순회로 풀면됨...아주 간단했음...
def preorder(n):
    global cnt
    if n > 0:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T + 1):
    # 간선의 개수, 노드의 번호
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    # 자식노드로 부모 인덱스 저장
    # 간선의 개수가 노드보다 하나 적고, 1부터 인덱스에 넣기위해 e+2로 함
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    # 연결된 노드 수를 세기 위해
    cnt = 0
    for i in range(E):
        p = tree[i * 2]
        c = tree[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    print('#{} {}'.format(tc, preorder(N)))