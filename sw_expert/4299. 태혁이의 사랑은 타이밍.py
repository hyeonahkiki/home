import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    # 기준날을 각각 표시
    event_m = 11
    event_d = 11
    event_time = 11
    event_time2 = 11
    res = 0
    if event_m == D:
        if event_time == H and event_time2 == M:
            res = 0
        elif event_time > H:
            res = -1
    elif event_m != D:
        cal_d = (D - event_m) * 24 * 60
        cal_h = (H-event_time) * 60
        cal_m = (M - event_time2)
        res = cal_d + cal_h + cal_m
    print('#{} {}'.format(tc, res))