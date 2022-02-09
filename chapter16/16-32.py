'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''
n=int(input())
x=[]
y=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    tmp=list(map(int,input().split()))
    x.append(tmp)
y[0][0]=x[0][0]
for i in range(0,n-1):
    for j in range(i+1):
        y[i+1][j]= max(y[i][j]+x[i+1][j],y[i+1][j])
        y[i+1][j+1]= max(y[i][j]+x[i+1][j+1],y[i+1][j+1])

tmp=0
for i in range(n):
    tmp=max(y[n-1][i],tmp)
print(tmp)

