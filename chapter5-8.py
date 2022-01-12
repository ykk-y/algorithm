"""
DFS
내가 생각한 것:
바로 for문?
def dfs(graph) -> def dfs(graph,1) ?? visited도 포함해야 함..
visited = [False]*9 # []*N을 하면 원소가 N개 생김. 배열이 N개 생기는게 아님..

"""

graph = [
    [],
    [2,3,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
def dfs(graph,v,visited):
    #v노드 방문 확인
    if visited[v] == True:
        return #?
    visited[v] = True
    print(v)
    for i in graph[v]:
        #다음 노드로 감 #방문했다면 #방문안했다면
        dfs(graph,i,visited)
'''
결과..
1
2
4
3
5
7
8
'''
dfs(graph,1,visited)