#ACM 호텔
T=int(input())
for i in range(T):
    h,w,n=map(int,input().split())

    if n%h==0:
        y=h
    else:
        y=n%h

    while n>h*w:
        n-=h*w

    if n%h==0:
        x=n//h
    else:
        x=(n//h)+1

    if x<10:
        print(str(y)+str(0)+str(x))
    else:
        print(str(y)+str(x))
