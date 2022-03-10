def solve(N,M,A,B):
    dic ={}
    for i in range(N):
        dic[A[i]] = i
    c = [ i for i  in A]
    c.sort()
    c = c[N-M:]
    minVal = min(c)
    ind = []
    for i in c:
        ind.append(dic[i])
    minVal = min(c)
    sum =0
    for i in ind:
        sum = sum + B[i]
    return sum * minVal

print(solve(2,2,[6,10],[7,7]))
print(solve(2,2,[6,10],[7,7]))
