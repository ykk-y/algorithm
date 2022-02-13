N=int(input())
T=[0]
P=[0]
x=[0]*(N+1)
for i in range(N+1):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
for i in range(1,N+1):
    if x[T[i]]==0:
        x[T[i]]=P[i]
    else:
        if T[i]==1:
            x[i]=x[i-1]+P[i]