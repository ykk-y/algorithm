n=int(input())
m=int(input())
INF=int(1e9)
x=[[INF]*(1+n) for _ in range(1+n)]
for i in range(m):
    a,b,c=map(int,input().split())
    if c < x[a][b]:
        x[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            x[a][b] = min(x[a][b],x[a][k]+x[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            x[i][j]=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if x[i][j]==INF:
            print('??')
            print(0, end=' ')
        else:
            print(x[i][j],end=' ')
    print()


'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''