'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''
import sys
N=int(input())
planet=[]
for i in range(N):
    x,y,z=map(int,sys.stdin.readline().split())
    planet.append((x,y,z))
edges=[]

for i in range(N):
    for j in range(i+1,N):
        cost=min(abs(planet[i][0]-planet[j][0]),abs(planet[i][1]-planet[j][1]),abs(planet[i][2]-planet[j][2]))
        edges.append((cost,i,j))

parent=[i for i in range(N)]
edges.sort()
def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find(parent,a)
    b = find(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
result=0
for edge in edges:
    cost,A,B=edge
    if find(parent,A)!=find(parent,B):
        union(parent,A,B)
        result+=cost
print(result)