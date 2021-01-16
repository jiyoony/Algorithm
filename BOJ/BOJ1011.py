#Fly me to the Alpha Centauri
t=int(input())
for i in range(t):
    x,y=map(int,input().split())

    if (y-x)==1:
        print(1)
    else:
        k=2 #이동횟수
        x+=1
        q=1 #이동거리
        while True:
            if (y-x-1)>= (q+1):
                x=x+q+1
                k+=1
                q+=1
                break
            elif (y-x-1) ==q:
                x=x+q
                k+=1
                break
            elif (y-x-1)==(q-1):
                x=x+q-1
                k+=1
                q-=1
                break
        print(k)
