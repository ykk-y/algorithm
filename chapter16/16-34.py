N=int(input())
x=list(map(int,input().split()))
y=[0]*(N)
y[0]=1
for i in range(1,N):
    if x[i-1]>x[i]:
        y[i]=y[i-1]+1
    else:
        j=i-2
        while x[j]<x[i] and j>=0:
            j-=1
        if j==-1:
            y[i]=1
        else:
            y[i]=y[j]+1
print(N-max(y))
'''
7
15 11 4 8 5 2 4
'''