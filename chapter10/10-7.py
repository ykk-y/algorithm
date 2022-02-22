'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

'''


def union(parent,a,b):
    a=find(parent,a)
    b = find(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

N,M=map(int,input().split())

parent=[i for i in range(N+1)]

for i in range(M):
    n, a, b = map(int,input().split())
    if n ==0:
        union(parent,a,b)
    else:
        if find(parent,a) != find(parent,b):
            print('NO')
        else:
            print('YES')
