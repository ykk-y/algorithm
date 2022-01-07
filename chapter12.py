'''
7
8: 헉 isalpha()로 바로 알파벳인지 검사가능
    문자열도 sort가능.
    문자열 하나로 합쳐서 보여주는 방법=> ''.join(리스트) =>이렇게 하면 리스트 사이사이에 아무것도 넣지 않겠다는 의미
9: 중간에만 일치하는 경우도 생각해서 너무 복잡하게 생각했는데, 마지막 제한사항을 확인해보았어야 했음
    문자열을 자르고, 비교하는 방법?
11: 맵, 사과 위치, 뱀의 이동 위치  모든걸 따로 변수를 만들어서 하려니 합치기가 너무 힘들고 if문을 작성하기 힘든것 같음..
    최대한 하나로 표현할 수 있도록 만들어야 겠음
    "방향" 이 있다는 건, x,y위치를 한번 생각해보면 좋을듯
    코드가 길어지면 복잡하니까 기능이 들어간 함수로 따로 빼서 사용해보기
'''
def solution_11(): #뱀의 몸길이?.. 머리, 꼬리 위치..?
    N=int(input())
    K=int(input()) #사과 위치
    apple=[]
    for _ in range(K):
        #apple.append(list(map(int, input().split()))) #들어갈때 리스트로 들어가려면 list 해줘야 함.. 튜플?
        apple.append(list(map(int, input().split())))
    L=int(input()) # 몇개 있는지
    loc=[]
    for _ in range(L):
        tmp=list(input().split())
        tmp[0]=int(tmp[0])
        loc.append(tmp)
    for n in range(L):
        time=loc[n][0] #초 받고 , 위치 이동
        for _ in range(time):#초???
            pass
        d=loc[n][1]


    for i in range(N):
        for j in range(N):
            pass

solution_11()


def solution_9():
    x = input()

solution_9()

def solution_7():
    lucky = input()
    cnt = int(len(lucky)/2)
    left=0
    right=0
    for i in range(cnt):
        left += int(lucky[i])
        right += int(lucky[-1-i])
    #왼쪽 더하기
    #오른쪽 더하기
    #출력
    if left == right:
        print('LUCKY')
    else:
        print('READY')
#solution_7()

def solution_8():
    x = input() #숫자 찾기, #문자 찾기..
    n=0
    m=[]
    for i in range(len(x)):
        if ord(x[i]) < ord('A'):# 숫자라면 더하기
            n += int(x[i])
        else :#문자라면 순서대로..
            m.append(x[i])

    m.sort()
    if n!=0:
        m.append(str(n))
    #print(m) #하나씩 출력되는데.. 문자열 하나로 합쳐서 보여주는 방법..

    print(''.join(m))
solution_8()