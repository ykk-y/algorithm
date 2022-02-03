'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
def dfs(map_,M,N,cnt,x,y,dir,d):
    if x<1 or x>=M-1 or y<1 or y>=N-1:
        return None
    map_[x][y]=2
    tmp=0
    is_break=False
    for data in range(4):
        tmp=data
        i,j=dir[d-data]
        if map_[x+i][y+j]==0:
            cnt += 1
            is_break=dfs(map_,M,N,cnt,x+i,y+j,dir,d-data+4)
    if tmp==3:
        i,j= x-dir[d][0],y-dir[d][1]
        if map_[i][j]==0:
            is_break=dfs(map_,M,N,cnt,i,j,dir,d)
        else:
            if not is_break:
                print(cnt)
            return True

def solution_1():
    N, M = map(int, input().split())
    A, B, d = map(int, input().split())
    map_ = []
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서   #왼쪽으로 회전. 북 서 남 동 0 : 인덱스 -1 씩 움직임
    for i in range(N):
        tmp = list(map(int, input().split()))
        map_.append(tmp)
    cnt = 1
    dfs(map_,M,N,cnt,A, B,dir,d)

solution_1()