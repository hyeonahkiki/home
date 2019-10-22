import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 2):
    N = int(input())
    origin = list(input().split())
    order_cnt = int(input())
    orders = list(input().split())
    I_num = []
    re_orders = []
    for i in range(len(orders)):
        if orders[i] =='I':
            I_num.append(i)
    for i in range(len(I_num)-1):
        re_orders.append(orders[I_num[i]:I_num[i+1]])
    re_orders.append(orders[I_num[-1]:])
    for order in re_orders:
        spot = int(order[1])
        cnt = int(order[2])
        nums = order[3:]
        k = 0
        if k < cnt:
            for num in nums:
                origin.insert(spot+k, num)
                k += 1
    print('#{} {}'.format(tc, ' '.join(origin[:10])))


