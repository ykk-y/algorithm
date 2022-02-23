'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
import sys
N,M=map(int,input().split())
edges=[]
for i in range(M):
    input = sys.stdin.readline().rstrip()
    a,b,cost = map(int,input.split())
    edges.append((cost,a,b))
parent=[0]*(N+1)
for i in range(1,N+1):
    parent[i]=i

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

edges.sort()
result=0
max_=0
for i in edges:
    c,a,b=i
    if find(parent,a)!=find(parent,b):
        union(parent,a,b)
        result+=c
        max_=c
result-=max_
print(result)
