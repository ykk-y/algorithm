'''
7
8: 헉 isalpha()로 바로 알파벳인지 검사가능
    문자열도 sort가능.
    문자열 하나로 합쳐서 보여주는 방법=> ''.join(리스트)

'''
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