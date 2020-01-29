import sys
sys.stdin = open('input', 'r')

def op_insert(n, p, k, op_remain):
    global op_case_set

    if n == k:
        op_case_set.append(p)
        return
    else:
        for idx in range(4):
            if op_remain[idx] == 0:
                continue
            else:
                op_remain_copy = op_remain[:]
                op_remain_copy[idx] -= 1
                op_insert(n+1, p + [idx], k, op_remain_copy)
        return

N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

op_case_set = []

op_insert(0, [], N-1, operator)

maxV = -1000000000
minV = 1000000000

for op_case in op_case_set:
    num_case = nums[:]
    for i in range(N-1):
        left = num_case[i]
        right = num_case[i+1]
        if op_case[i] == 0:
            num_case[i + 1] = left + right
        elif op_case[i] == 1:
            num_case[i + 1] = left - right
        elif op_case[i] == 2:
            num_case[i + 1] = left * right
        else:
            if left < 0:
                left *= -1
                num_case[i + 1] = (left // right) * -1
            else:
                num_case[i + 1] = left // right

    if num_case[-1] > maxV:
        maxV = num_case[-1]
    if num_case[-1] < minV:
        minV = num_case[-1]
print(maxV)
print(minV)