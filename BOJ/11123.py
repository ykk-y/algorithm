import sys
from collections import deque
T=int(sys.stdin.readline().strip())
def bfs(graph,visit,start):
    dir =[(0,1),(1,0),(0,-1),(-1,0)]
    x,y=start
    q=deque([(x,y)])
    visit[x][y]=True
    while q:
        x,y=q.popleft()
        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if nx>=0 and ny>=0 and nx<H and ny<W:
                if not visit[nx][ny]:
                    if graph[nx][ny]=='#':
                        visit[nx][ny]=True
                        q.append((nx,ny))
for i in range(T):
    H, W = map(int, sys.stdin.readline().split())
    graph=[]
    visit=[[False]*W for _ in range(H)]
    for i in range(H):
        graph.append(list(sys.stdin.readline().strip()))
    cnt=0
    for x in range(H):
        for y in range(W):
            if not visit[x][y]:
                if graph[x][y]=='#':
                    bfs(graph,visit,(x,y))
                    cnt+=1
    print(cnt)