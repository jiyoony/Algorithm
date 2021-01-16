#펙토리얼
n=int(input())
def fac(k):
    if k==0:
        return 1
    if k==1:
        return 1
    else:
        return k*fac(k-1)
print(fac(n))
