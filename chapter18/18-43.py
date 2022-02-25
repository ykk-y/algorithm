'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''
import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N ==0 and M==0:
        break
    edges = []
    tot_cost = 0
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append((c, a, b))
        tot_cost += c
    parent = [i for i in range(N)]

    result_cost = 0
    edges.sort()

    for edge in edges:
        c, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result_cost += c
    print(tot_cost - result_cost)

