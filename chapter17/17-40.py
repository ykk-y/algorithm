import heapq
N,M=map(int,input().split())
INF=int(1e9)
start=1
graph=[[] for i in range(N+1)]
distance= [INF]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a, 1))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now =heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

for i in range(0,N+1):
    if distance[i]==INF:
        distance[i] =0
m = max(distance)
index=-1
for i in range(1,N+1):
    if distance[i]==m:
        index=i
        break
cnt=distance.count(m)
print(index,m,cnt)

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''