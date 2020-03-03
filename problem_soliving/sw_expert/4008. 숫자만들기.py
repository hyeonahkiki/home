import sys

sys.stdin = open('input.txt', 'r')


# 계산할 첫번째 값, 기호가 숫자가 들어간 리스트
def cal(first, s, op_list):
    if op_list[0]> 0:
        op_list[0] -= 1
        cal(first, s+first, op_list)
        op_list[0] += 1
        return s
    if op_list[1] > 0:
        op_list[1] -= 1
        cal(first, s-first, op_list)
        op_list[1] += 1
        return s
    if op_list[2] > 0:
        op_list[2] -= 1
        cal(first, s*first, op_list)
        op_list[2] += 1
        return s
    if op_list[3] > 0:
        op_list[3] -= 1
        cal(first, s/first, op_list)
        op_list[3] += 1
        return s




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # +, -, *, /
    sign = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # 최대값과 최소값의 차이를 알아야함
    minV = 10000000
    maxV = -10000000
    if maxV < cal(nums[0], 0, sign):
        maxV = cal(nums[0], 0, sign)
    if minV > cal(nums[0], 0, sign):
        minV = cal(nums[0], 0, sign)
    print('#{} {}'.format(tc, maxV-minV))

