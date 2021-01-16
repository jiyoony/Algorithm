#평균
n=int(input())
sco=list(map(int,input().split()))
scob=sorted(sco)
best=scob[n-1]
newsco=sco.copy()
whole=0
for j in range(n):
    newsco[j]=newsco[j]/best*100
for i in range(n):
    whole+=newsco[i]
print(whole/n)
