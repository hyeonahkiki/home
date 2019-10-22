import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 사람 수 , 시간, 만든개수
    N, M, K = map(int, input().split())
    # 손님 방문시간
    guest = sorted(list(map(int, input().split())))
    # 붕어빵
    bread = 0
    # 시간의 경과가 필요
    time = M
    ans='Impossible'
    while guest:
        if guest[0] < M:
            break
        else:
            if time < guest[0]:
                if time % M ==0:
                    bread += K
                time += 1
            elif time % M ==0:
                bread += K
                if bread:
                    bread-= 1
                    time += 1
                    guest.pop(0)
                else:
                    break
            else:
                if bread:
                    bread-= 1
                    time += 1
                    guest.pop(0)
                else:
                    break
    if bread >=0 and len(guest)==0:
        ans = 'Possible'
    print('#{} {}'.format(tc, ans))
