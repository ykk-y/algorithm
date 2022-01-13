graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
from collections import deque
visited=[False]*9
def dfs(graph,start,visited):
    queue=deque([start])
    while queue:
        v = queue.popleft()
        #visited[v] = True
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[v] = True #방문처리를 하는건, 큐에서 빠져나왔을 때 하는게 아니라 큐에 넣을 때?

dfs(graph,1,visited)
'''
1 2 3 8 7 4 5 [7]
'''