'''
5
-15 -6 1 3 7
왜 return 하면 none이지..
아 찾았을 때  return mid 할 것만이 아니라,
다른 조건문 x[mid] > mid, x[mid] < mid에서도 "return binary_sort()" 해줘야 함.. 그냥 binary_sort()해줬음,,
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