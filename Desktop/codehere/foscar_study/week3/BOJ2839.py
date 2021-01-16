#설탕배달
n=int(input())
cnt=0

while (n%5!=0 and n>2):
    n-=3
    cnt+=1
if (n%5==0):
    cnt+=n/5
    print(int(cnt))
else:
    print(-1)
