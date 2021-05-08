A = [1,2,3,4,5,6,7,8]
#A = [1,3,7,11,12,14,18]

dp = {}
ret = 0
for i in range(1, len(A)):
    for j in range(i):
        diff = A[i] - A[j]
        # (7, 11): 4
        if diff < A[j] and diff in A:
            dp[(A[j],A[i])] = dp.get((diff,A[j]), 2) + 1
            ret = max(ret, dp[(A[j],A[i])])

print (ret)
print (dp)
