#세 수
a,b,c=map(int,input().split())
if  a>=b>c:
    print(b)
elif b>=a>c:
    print(a)
elif c>=a>b:
    print(a)
elif c>=b>a:
    print(b)
else:
    print(c)
