#x보다 작은 수
n,x=map(int,input().split())
a=[]
a = list(map(int,input().split()))
for i in range(n):
    if a[i]<x:
        print(a[i],end=' ')

'''
#x보다 작은 수
n,x=map(int,input().split())
a=[]
for i in range(10):
    a.append(int(input()))
for i in range(n):
    if a[i]<x:
        print(a[i])
#틀린이유
리스트에서 값을 여러개 입력받을 때
for문으로 a.append()가 아닌
a=list(map(int,input().split()))을 써야함

'''
