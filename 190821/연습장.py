n, k = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
cntk = 0

while i < n :
    while i< n and arr[0]==0:
        i += 1
    cnt = 0
    while i<n and arr[i]==1:
        cnt +=1
        i += 1
    if cnt ==k:
        cntk +=1
print(cntk)
