import sys
import copy
from collections import deque
N=int(input())
indegree=[0]*(N+1)
graph=[]
time=[0]*(N+1)
for i in range(N):
    x=list(map(int,input().split()))
    time[i+1]=x[0]
    for j in x[1:-1]:
        graph[j].apend(i)
        indegree[i]+=1

def topology_sort():
    q=deque()
    result=copy.deepcopy(time)
    max_=-1
    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)