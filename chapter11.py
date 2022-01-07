"""
1: 정렬, 문제 잘 읽기('최대' 몇개의 그룹임. 최대 사람 수가 아님..)
    ... 어떻게 비교하지... 카운트 변수 하나만으로는 힘들겠다
    =>갯수, 해당 숫자, result 에 대한 변수를 정해놓아야 비교가 가능할 것 같다.

2. for문에서 처음 변수를 어떻게할지 고민했는데 그냥 for문 밖에서 한번 해주면 되는것 같다.
3. 0과 1이 등장한 수를 각각 세어주고, 이전값과 비교하는 것이기 때문에 마지막에서 따로 빼서 다시 비교함
    => 첫번째와 가장 마지막을 생각해주기
4. ??
5. 내가 푼건 완전탐색. 그리디는..
"""
#5 3
#1 3 2 3 2

#8 5
#1 5 4 3 2 4 5 2

def solution_5():
    N,M=map(int,input().split())
    x=list(map(int,input().split()))
    x.sort()
    result=0
    for i in range(N):
        for j in range(i+1,N):
            if x[i]!=x[j]:
                result+=1
    print(result)
solution_5()

def solution_4():
    is1=0#처음에 1이 안만들어지는 경우
    isnot1=0# 처음에 1이 만들어지는 경우
    N=int(input())
    x = list(map(int,input().split()))
    x.sort()
    num=1
    if x[0] !=1: # 맨처음이 1보다 큰 경우
        print(1)
    else: # 맨처음이 1
        for i in range(len()): #처음에 보는 개수?
            for i in range(len(x)): # 1 2 3 4 5
                num+=1
                n = x[i]




def solution_3():
    S = input()
    is_0= 0
    is_1= 0
    n=int(S[0])
    for i in range(1,len(S)):
        num=int(S[i])
        if n == num:  #연속인 수 찾기.. 같으면
            pass
        else:   #다르면
            if n == 0: # #이전이 0이면
                is_0 +=1
            else:
                is_1 +=1 #이전이 1이면
        n = num

    if S[-2] != S[-1]:
        if S[-1]==0:
            is_0 +=1
        else:
            is_1 +=1

    if is_0 < is_1:
        print(is_0)
    else:
        print(is_1)

solution_3()

#02984
def solution_2():
    x = input()
    result=int(x[0]) #맨 처음은..?
    for i in range(1,len(x)):
        n = int(x[i])
        if result==0 or result==1: #0이나 1이면 더하기, 나머지는 곱하기
            result += n
        else :
            result *= n
    print(result)


solution_2()


#5
#2 3 1 2 2

def solution_1():
    N = int(input())
    x = list(map(int,input().split()))
    x.sort()
    cnt=1
    result=0
    for i in range(N):
        n = x[i]
        if n == cnt: #해당 숫자의 갯수만큼을..? 1이면 1개만, 2면 2개만 3이면 3개만 ..
            result+=1
            cnt=1
        else: # 1 1 2 3 3
            cnt+=1
    print(result)


#solution_1()