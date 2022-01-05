"""
잘 모르겠는 부분
4-1
방향 표현을 딕셔너리 생각했는데..
          인덱스로 한다면 인덱스에 해당하는걸 어떻게 표현해야하지
          그리고 어떻게 찾지? 인덱스가 같은걸 찾는방법? 처음에는 입력받은 문자열을 이용해서 같은 타입을 찾는걸로 생각했지만.. 그 다음은?

4-2
시간 표현? => 일치하는 것 찾는건 숫자 대신 문자열(in)
다..세기? => 100만개 기준으로는 완전탐색도 생각해보기

4-3
1번한 뒤 2번을 하는건줄 알았지만, 1번 또는 2번이 따로 가능한지를 확인하는 문제
    ->만약 이렇다면, 한 단계라도 벗어난 경우를 또 생각해서 if문으로 쪼개야 할듯 함. 합쳐서 하면 다시 체스판 안으로 들어오게 되는 경우가 생김

char 표현을 ? -> 숫자로 바꾸기.. => ord() - ord('a')+1 => +1까지 해야 a부터 포함
if 조건이 1부터인지, 0부터인지 확인

4-4
input()은 str .. map은 list 아니어도 가능
1) 방향에 어떤 의미가 있지?=?인덱스 위치계산 ) 지나간 위치 표현은 어떻게 하지?
3) 각 줄을 입력받고 확인하는 방법? 전체를 입력받고 확인하는 방법?
"""
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
def solution_4():
    N, M = map(int, input().split())
    x, y, d = map(int, input().split())
    #data = [0 for _ in range(N*M)]
    #data = [ [0]*M  for _ in range(N)] # [[0]*개수] 를 해주면, 한 행에 N개의 요소를 갖는 배열이 생성됨 [0,0,0,0].    이거 아님[[0],[0],[0],[0]]
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))  # 단순히 list를 대입하면 한줄밖에 안들어감

#    for i in range(N):
#       data = list(map(int, input().split())) # 단순히 list를 대입하면 한줄밖에 안들어감
    #첫 육지를 찾아야하는데, 무조건 육지의 시작이 1,1에 있지 않을 수 있기 때문에, 처음에 다 입력받아야 할것같음
    #방향을 볼 때도 한줄씩 입력받으면 문제생길것 같음
    #왼쪽?? 파이썬은 음수도 가능하니 다행..
    # 0일때 인덱스는 x,y-1 북->서
    # 1 : x+1, y 동->남
    # 2 : x, y+1 남->동
    # 3 : x-1, y 서-> 남
    is_stop=False
    cnt=0
    dxy=[(0,-1),(1,0),(0,1),(-1,0)]
    for i in range(1,N):
        for j in range(1,M):
            for k in range(1,5):
                dx, dy=dxy[d-k][0], dxy[d-k][1] #방향의 왼쪽을 봄
                if data[x + dx][y + dy] == 0: #만약 바라본 방향이 안가본 육지라면
                    data[i][j] = 1  #현재칸을 1(가본곳 처리)
                    x, y = dx, dy  # 이동할 곳으로 지정(index)
                    cnt +=1
                elif k==4 : #뒤???바라보는 방향과 관련..dx dy가 앞을 보는거
                    x ,y = -dx, -dy
                    cnt -=1
                    if  x==0 or x == N or y==0 or y==M :                 #만약 다 돈 것이고, 갈데가 없고 뒤가 바다이면
                        is_stop=True
            if is_stop:
                print(cnt)
                break
        if is_stop:
            break
                # 만약 다 돈 것이고, 갈데가 없고 뒤가 바다가 아니라면
                # 가봤다면 continue

solution_4()


# L R U D
def solution_1(): #문제는 너무 반복적으로 복붙한 if문이 많음.. tmp와 일반변수 역할이 조금 중복됨.. list(input().split())는 안됨..
    N = int(input())
    walk = input().split()
    move = [(0,-1),(0,1),(-1,0),(1,0)]
    x , y = 1,1
    tmpx, tmpy = 1,1
    for w in walk:
        tmpx = x
        tmpy = y
        if w =='L':
            tmpx += move[0][0]
            tmpy += move[0][1]
        elif w == 'R':
            tmpx += move[1][0]
            tmpy += move[1][1]
        elif w == 'U':
            tmpx += move[2][0]
            tmpy += move[2][1]
        else:
            tmpx += move[3][0]
            tmpy += move[3][1]

        if tmpx<1 or tmpx>N or tmpy<1 or tmpy>N:
            continue
        else:
            x = tmpx
            y = tmpy
    print(x,y)

#solution_1()

# 시: 03, 13, 23
# 분: 03, 13, 23, 33, 43, 53
# 초: 03, 13, 23, 33, 43, 53
def solution_2(): #어라 ..? 모가 틀린거지.. -> 아 5959까지인데, 그 다음까지 세어버리는군 어라?->아 5960까지 되네 -> +1 해주기..?
    N = int(input()) #자릿수표현? 한자릿수 시간, 두자릿수 시간..
    cnt = 0
    for h in range(N+1): #몇번을 도는건지 어떻게 표현하지??
        for m in range(60):
            for s in range(60):
                if '3' in str(h)+str(m)+str(s):
                    cnt+=1
    print(cnt)

#solution_2()

def solution_3(): #틂린 풀이.. 1과 2를 연달아 계산하는 경우는 밖에 나갈때마다 제외해줘야 함
    pos = input()
    move1 = [(2,1),(2,-1),(-2,1),(-2,-1)]
    move2 = [(1,2),(1,-2),(-1,2),(-1,-2)]
    cnt = 0
    for i in range(4):
        x, y = int(ord(pos[0]) - ord('a') + 1), int(pos[1])
        tmpx = x+move1[i][0]
        if tmpx < 1 or tmpx > 8:
            continue
        tmpy = y+move1[i][1]
        if tmpy < 1 or tmpy > 8:
            continue
        x = tmpx
        y = tmpy
        for j in range(4):
            tmpy = y + move2[j][1]
            if tmpy < 1 or tmpy > 8:
                continue
            tmpx = x + move2[j][0]
            if tmpx < 1 or tmpx > 8 :
                continue
            cnt +=1
    print(cnt)
#solution_3()

def solution_3_2():
    pos = input()
    move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    cnt = 0
    for i in range(8):
        x, y = int(ord(pos[0]) - ord('a') + 1), int(pos[1])
        tmpx = x+move[i][0]
        if tmpx < 1 or tmpx > 8:
            continue
        tmpy = y+move[i][1]
        if tmpy < 1 or tmpy > 8:
            continue
        cnt +=1
    print(cnt)

#solution_3_2()
