"""
1: 정렬, 문제 잘 읽기('최대' 몇개의 그룹임. 최대 사람 수가 아님..)
    ... 어떻게 비교하지... 카운트 변수 하나만으로는 힘들겠다
    =>갯수, 해당 숫자, result 에 대한 변수를 정해놓아야 비교가 가능할 것 같다.
"""
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


solution_1()