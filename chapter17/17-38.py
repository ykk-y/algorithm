N,M=map(int,input().split())
INF=int(1e9)
# 1~k까지 연결된곳이 있는지, k이후가 있는지.. 플로이드워셜
# 거리 비용은 상관없이 0 또는 INF가 아닌곳을 찾기
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
x= [[INF]*(N+1) for _ in range(N+1)]
for i in range(1,M+1):
    a,b=map(int,input().split())
    x[a][b]=1

for i in range(1,M+1):
    for j in range(1,M+1):
        if i==j:
            x[i][j]=0

for k in range(1,M+1):
    for a in range(1, M + 1):
        for b in range(1, M + 1):
            x[a][b] = min(x[a][b],x[a][k]+x[k][b])
cnt=0
'''for i in range(M+1):
    for j in range(M+1):
        if x[i][j]==INF:
            x[i][j]
'''
for i in range(1,M+1):
    if x[i].count(0)+x[i].count(INF)==M-1:
        cnt+=1
print(cnt)

