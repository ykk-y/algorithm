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
"""
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

def solution_3():
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

solution_3_2()