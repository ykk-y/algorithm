'''
5
-15 -6 1 3 7
왜 return 하면 none이지..
아 찾았을 때  return mid 할 것만이 아니라,
다른 조건문 x[mid] > mid, x[mid] < mid에서도 "return binary_sort()" 해줘야 함.. 그냥 binary_sort()해줬음,,
처음에 헷갈렸던 부분은, 기준을 어디로 하는건지 였는데, 리스트 길이를 인덱스와 비교할까 음수부터 제외할까 하다가,
이진탐색으로 찾아가면서 x[index] 를 index와 비교하는 방법을 생각해봄
처음에 의심한건, 그럼 더 오른쪽으로 가거나 왼쪽으로 가면 규칙을 벗어나는건 .. 없나? 였는데
무조건 맞다. 왜냐면 오름차순으로 정렬되어있기 때문에, 이미 한곳에서 틀어졌다면 뒤에는 수가 계속 커지게 될 것이기 때문
'''

N=int(input())
x=list(map(int,input().split()))
def solution_1():
    ret=b_s(0,N-1)
    if ret==None:
        print(-1)
    else :
        print(ret)

def b_s(start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if x[mid] > mid:
        return b_s(start,mid-1)
    elif x[mid] < mid:
        return b_s(mid+1,end)
    else:
        return mid

solution_1()