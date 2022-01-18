'''
2
kim 50 60 100
soong 80 60 50
'''
N=int(input())
student=[]
x=[]
for i in range(N):
    student.append(input().split())
    #x.append(input().split())

student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) # lambda 쓸때 =()
for i in range(N):
    print(student)