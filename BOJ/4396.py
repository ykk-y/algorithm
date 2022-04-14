import sys
from collections import deque
N = int(sys.stdin.readline().strip())
graph=[]
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))
#t_visit=[[False]*N for i in range(N)]
x_visit=[]
for i in range(N):
    x_visit.append(list(sys.stdin.readline().strip()))
#방문한 위치라면, 8방향 조사하기
#지뢰 없으면서 방문칸엔 숫자
#지뢰 있는 방문칸이라면 모든 지뢰칸이 별표로 표시되어야 함
result=[['.']*N for i in range(N)]
dir=[(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
def search(start):
    x,y=start
    cnt=0
    if graph[x][y]=='*':
        result[x][y]='*'
        return True
    else:
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if graph[nx][ny] == '*':  # 8칸을 조사하는데
                    cnt += 1  # 만약 지뢰가 열렸다면 별표시를 하기
        result[x][y] = cnt  # 아니라면 지뢰 숫자 세기
        return False
check=False
for i in range(N):
    for j in range(N):
        if x_visit[i][j]=='x':
            if search((i,j)):
                check=True
for i in range(N):
    for j in range(N):
        if check:
            if graph[i][j]=='*' and x_visit[i][j]=='.':
                result[i][j]='*'
        if j<N-1:
            print(result[i][j],end='')
        else:
            print(result[i][j])