'''
BFS
'''

from collections import deque
deque = deque #위치?

def bfs(graph, start, visited):
    #방문체크
    queue = deque([start]) # 원소들 넣는단 의미?
    print(queue)
    visited[start]=True
    #for i in graph[start]: #노드추가
    while queue: #큐에 있는지 없는지로 판단,, for 대신 while을 쓰는건, popleft 때문에 인덱스 이동
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]: #아직 방문하지 않은 노드 삽입
            if not visited[i]: #방문하지 않았다면
                queue.append(i)
                visited[i]=True #이건 queue라는 배열이 무한반복이기 때문에 bfs를 반복하지 않아도 됨


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
visited=[False]*9
bfs(graph,1,visited)
