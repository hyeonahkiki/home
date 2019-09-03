tc = int(input())
sample = list(map(int, input().split()))
ans = []
i = 0
j = i+1
for t in range(tc):
    if sample[i] < sample[j]:
        ans.append(sample[j])
        i += 1
    elif sample[i] > sample[j]:
        if j <tc-1:
            j += 1
            sample[i] < sample[j]
            ans.append(sample[j])
        elif j ==tc -1:
            ans.append(-1)
    else:
        ans.append(-1)
print(ans)

n = int(input())
nums = list(map(int, input().split()))
res = []
for i in range(n):
    j = 1
    if i == n-1 or nums[i] >= max(nums[i+1:]):
        res.append('-1')
    else:
        if nums[i]:
            while nums[i] >= nums[i + j]:
              j += 1
               res.append(str(nums[i + j]))

print(' '.join(res))



