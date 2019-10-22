import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hays = []
    for i in range(N):
        hay = int(input())
        hays.append(hay)
    average = sum(hays) // len(hays)
    # 같게하려면 최소 움직임
    move = 0
    re_hays = sorted(hays)
    for re in re_hays:
        if re < average:
            ans = average - re
            move += ans
    print('#{} {}'.format(tc, move))