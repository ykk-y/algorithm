'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
import sys
N,M=map(int,input().split())
x=[]
for i in range(N):
    x.append(list(map(int,sys.stdin.readline().split())))
parent=[i for i in range(N+1)]
edges=[]
cnt=0
for i in range(N):
    for j in range(N):
        if x[i][j]==1:
            edges.append((i+1,j+1))
            cnt+=1
tour=list((map(int, sys.stdin.readline().split())))
def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find(parent,a)
    b = find(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a] = b

for i in range(cnt):
    a,b=edges[i]
    union(parent,a,b)

where_=tour[0]
p_union=parent[where_]
is_ok=True
for i in range(2,M):
    if p_union!=parent[i]:
        is_ok=False
if is_ok:
    print("YES")
else:
    print("NO")


