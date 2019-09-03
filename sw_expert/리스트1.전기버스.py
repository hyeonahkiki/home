T = int(input())
for tc in range(1, T+1):
    max_move, station_num, battery = map(int, input().split())
    stations = list(map(int, input().split()))
    final_stations = [0] + stations +[station_num]
    cnt = 0
    last = final_stations[0]

    for i in range(1, len(final_stations)):
        if final_stations[i] - final_stations[i-1] > max_move:
            cnt = 0
            break
        elif final_stations[i]-last > max_move:
            cnt += 1
            last = final_stations[i-1]
    print('#{} {}'.format(tc, cnt))

