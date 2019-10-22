import sys
sys.stdin = open('input.txt', 'r')

# 양 끝쪽을 제외하고 건물을 5개씩 묶어서 cnt
# 건물에서 젤 큰건물과 그다음 큰 건물의 차이만큼의 세대는 조망권 확보

for tc in range(1, 2):
    N = int(input())
    buildings = list(map(int, input().split()))
    # 조망권 확보 세대 수
    cnt = 0
    # 5채씩 묶어서 확인해보기(조망권 확보가 양쪽 2칸씩)
    build_5 = []
    for i in range(len(buildings)-4):
        build_5.append(buildings[i:i+5])
    for building in build_5:
        middle = building[2]
        if max(building) == middle:
            check = sorted(building, reverse=True)
            ans = check[0] - check[1]
            cnt += ans
    print('#{} {}'.format(tc, cnt))



