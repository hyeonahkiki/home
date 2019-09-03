#sw expert - stack2 그래프경로

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    roads = [list(map(int, input().split())) for x in range(e)]
    s, g = map(int, input().split())
    stack = []
    res = 0

    for i in range(e):
        if roads[i][0] ==s:
            stack.append(roads[i]) # 시작점을 찾으면 넣기
            roads.pop(i) # 찾은점을 지워줌(나중에 도착점을 찾거나하면...또 for문을 써야하니까)
            break # 시작점을 찾으면 브레이크

    while len(stack)!=0:
        pick = stack.pop() # while문을 빠져나와야하기 때문에 조건을 넣어줘야함
        if pick[1] == g:
            res = 1
            break
        else:
            for i in range(len(roads)):
                if pick[1] == roads[i][0]: #[1, 4]였을 때 4가 다시 시작점이 됨
                    stack.append(roads[i])
    print('#{} {}'.format(tc, res))