#더하기 사이클
n=int(input())
t=0
a=n
while True:
    if n<10:
        n=n*11
        t+=1
    else:
        n=(n%10+n//10)%10+n%10*10
        t+=1
    if a==n:
        print(t)
        break
