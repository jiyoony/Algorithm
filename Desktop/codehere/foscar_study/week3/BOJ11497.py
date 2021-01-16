# import numpy as np
# #통나무 건너뛰기
# t=int(input())
# odd=[]
# even=[]
# for i in range(t):
#     n=int(input())
#     num=list(map(int,input().split()))
#     num.sort()
#     for k in range(n):
#             if (k%2==0):
#                 even.append(num[k])
#             else:
#                 odd.insert(0,num[k])
#     result=np.concatenate([even,odd])
#     cha=0
#     for p in range(n):
#         cha=max(cha,abs(result[p]-result[p-1]))
#     print(cha)
#     num.clear()
#     even.clear()
#     odd.clear()


#통나무 건너뛰기
t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    num.sort()
    cha=0
    for p in range(2,n):
        cha=max(cha,abs(num[p]-num[p-2]))
    print(cha)
