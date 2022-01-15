from collections import deque
N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)] # a도시 b 도시..? cost정보는 없으니까.. 행렬표현으로?
print(graph)
d=[0]*(N+1) #조건.. -1

for i in range(M):
    x,y = map(int,input().split())
    #graph.append((x,y)) #출발-도착
    #graph[x][y]=1
    graph[x].append(y)

def bfs(start):
    queue = deque()
     #큐에 들어가야하는게 어떤거지? #순서가 첫번째 말곤 없는데..? 아
    for a in range(start,N+1):
        queue.append(a)
    while queue:
        tmp = queue.popleft()
        for i in graph[tmp]: # 1 - 2,3
            if d[i]==0:
                d[i]=d[tmp]+1


    pass

bfs(X)
cnt=0
for k in range(N+1):
    if d[k]==K:
        print(k)
    else:
        cnt +=1
if cnt ==N+1:
    print(-1)

'''
4 4 2 1
1 2
1 3
2 3
2 4
'''