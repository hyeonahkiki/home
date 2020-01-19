import sys

sys.stdin = open('input', 'r')

# 계산 결과, 연산자의 리스트, 연산자의 개수
def check(n, lists, k):
    global maxV, minV, i
    if k ==0:
        if n> maxV:
            maxV = int(n)
        if n < minV:
            minV = int(n)
    else:
        if i < N:
            if info[0] != 0:
                info[0] -= 1
                i += 1
                check(n+nums[i], lists, k-1)
                info[0] += 1
                i -= 1
            if info[1] != 0:
                info[1] -= 1
                i += 1
                check(n-nums[i], lists, k-1)
                info[1] += 1
                i -= 1
            if info[2] !=0:
                info[2] -= 1
                i += 1
                check(n * nums[i], lists, k-1)
                info[2] += 1
                i -= 1
            if info[3] !=0:
                info[3] -= 1
                i += 1
                check(n / nums[i], lists, k-1)
                info[3] += 1
                i -= 1



N = int(input())
nums = list(map(int, input().split()))
# +, -, *, /
info = list(map(int, input().split()))
maxV = -1
minV = 100000
# 연산자의 수 세기
total = 0
i = 0
for j in info:
    if j !=0:
        total +=j
check(nums[0], info, total)
print(maxV)
print(minV)