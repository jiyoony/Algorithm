#부녀회장이 될테야
for _ in range(int(input())):
    k=int(input())
    n=int(input())
    v=[i for i in range(1,n+1)]
    for _ in range(k):
        for j in range(1,n):
            v[j]+=v[j-1]
    print(v[-1])


'''
#내가 푼것
#map.split()쓰면 런타임에러남......

t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    a=[[0]*(n+1)]*(k+1)

    for j in range(n+1):
        a[0][j]=j+1

    for q in range(1,k+1):
        a[q][0]=1

    for g in range(1,k+1):
        for p in range(1,n+1):
            a[g][p]=(a[g-1][p]+a[g][p-1])

    print(a[k-1][n-1])
'''
