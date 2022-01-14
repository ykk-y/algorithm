'''
5 6
101010
111111
000001
111111
111111
'''

from collections import deque
N,M=map(int,input().split())
graph=[]
for i in range(N):
   graph.append(list(map(int,input())))

def bfs(startx,starty):
    queue = deque() # deque((x,y)) 안되나..?
    queue.append((startx,starty))
    d=[(0,-1),(-1,0),(1,0),(0,1)]
    while queue: #빼기 #추가 #visited
        x,y =queue.popleft()
        for i in range(4):
            tmpx= x+d[i][0]
            tmpy= y+d[i][1]
            if tmpx <0 or tmpx>=N or tmpy<0 or tmpy>=M: #조건을 벗어난 경우?
                continue
            if graph[tmpx][tmpy]==0: #괴물이 있다면?
                continue
            if graph[tmpx][tmpy]==1:
                graph[tmpx][tmpy]= graph[x][y]+1
                queue.append((tmpx,tmpy))


bfs(0,0) # 시작칸 (1,1)은 배열에서 (0,0)인듯
print(graph[N-1][M-1])