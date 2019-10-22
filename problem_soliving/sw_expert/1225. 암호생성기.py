import sys
sys.stdin = open('input.txt', 'r')

for x in range(1, 11):
    tc = int(input())
    nums = list(map(int, input().split()))
    # 뺄 숫자 만들기
    k = 1
    while nums[-1] !=0:
        num=nums.pop(0)
        num -=k
        if num <=0:
            nums.append(0)
        else:
            nums.append(num)
        k += 1
        if k>5:
            k=1
    nums = list(map(str, nums))
    print('#{} {}'.format(tc, ' '.join(nums)))



