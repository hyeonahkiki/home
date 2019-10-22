import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 2):
    N = int(input())
    origin = list(input().split())
    order_cnt = int(input())
    orders = list(input().split())
    order_num = []
    re_orders = []
    for i in range(len(orders)):
        if orders[i] == 'I' or orders[i] == 'D' or orders[i] == 'A':
            order_num.append(i)
    for i in range(len(order_num) - 1):
        re_orders.append(orders[order_num[i]:order_num[i + 1]])
    re_orders.append(orders[order_num[-1]:])
    for order in re_orders:
        if order[0] == 'I':
            spot = int(order[1])
            cnt = int(order[2])
            nums = order[3:]
            k = 0
            if k < cnt:
                for num in nums:
                    origin.insert(spot + k, num)
                    k += 1
        elif order[0] =='D':
            spot2 = int(order[1])
            cnt2 = int(order[2])
            for x in range(cnt2):
                origin.pop(spot2)
        elif order[0] =='A':
            cnt3 = int(order[1])
            nums = orders[2:]
            for x in range(cnt3):
                for num in nums:
                    origin.append(num)
    print('#{} {}'.format(tc, ' '.join(origin[:10])))
