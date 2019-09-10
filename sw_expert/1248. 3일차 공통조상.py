import sys
sys.stdin = open('input.txt', 'r')


# 서브트리 cnt를 어떤 방법으로 할지 고민
# 아예 밑에까지 쭉들어가서 세는 전위 순회로함
def preorder(n):
    global cnt
    if n > 0:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T + 1):
    # 정점 수, 간선 수, 찾는점1, 찾는점 2
    V, E, num1, num2 = map(int, input().split())
    nodes = list(map(int, input().split()))
    par = [0] * (V + 1)
    # subtree의 개수를 세기위해서 생성. 순회를 이용할거라
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    cnt = 0
    # 자식 인덱스로 부모 저장
    # 짝수 인덱스에는 부모가 홀수 인덱스에는 자식이 오는 것을 이용
    for i in range(E):
        p = nodes[i * 2]
        c = nodes[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p

    # num1의 조상을 표시할 빈 배열을 생성
    check = [0] * (V + 1)
    # res가 공통 조상이 됨
    # num1의 조상을 체크
    ans = num1
    while par[ans] != 0:
        check[par[ans]] = 1
        ans = par[ans]
    # num2의 조상을 check배열에서 확인 1이어야 while문을 나올 수 있음
    # 처음만나는 1일 때 나오니까 그때가 가장 가까운 공통조상
    res = num2
    while check[res] == 0:
        res = par[res]

    preorder(res)
    print('#{} {} {}'.format(tc, res, cnt))
