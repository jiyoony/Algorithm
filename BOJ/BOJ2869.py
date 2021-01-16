#달팽이는 올라가고 싶다
a,b,v=map(int,input().split())
if (v-a)%(a-b)==0:
    print((v-a)//(a-b)+1)
else:
    print((v-a)//(a-b)+2)

'''
a,b,v=map(int,input().split())
day=0
high=0
while True:
    day+=1
    high+=a
    if high >=v:
        print(day)
        break
    high-=b
'''
