#설탕 배달
n=int(input())
c=0
while True:
    if n%5==0:
        c+=n//5
        print(c)
        break
    n-=3
    c+=1
    if n<0:
        print(-1)
        break
