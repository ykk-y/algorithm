# algorithm

chapter5-8 visited = [False]*9 # []*N을 하면 원소가 N개 생김. 배열이 N개 생기는게 아님..  
chapter5-9 BFS while:index changed(popleft), new array:queue(dequeue)  
chapter5-11 DFS graph: list(map(int,input())), move:index[x][y], -1/+1(o),+1+1(x), return: boundary, if-if-...return(pass)  
### BFS ? DFS ?
BFS: 최단거리..?  
DFS: 전부 둘러보기..?  
## stack vs queue: 스택/큐에 넣는 순간 방문한 것.
stack: 특별한 변수 추가는 없음. 스택에 입력출력 생각하지 않고 n_1 -> n_2 -> .. 진행된다고 생각해야할까 ..  하나만 넣기.  
queue: deque 변수 추가. (꺼낼 때 방문한게 아님) . 연관된건 다 넣기  
