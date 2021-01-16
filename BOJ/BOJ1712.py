#손익분기점
'''
# a,b,c=map(int,input().split())
# for i in range(1,210000000):
#     if a+i*b < i*c:
#         print(i)
#         break
#     else:
#         if b>=c:
#             print(-1)
#             break
'''

s=list(map(int,input().split()))
if s[1]>=s[2]:
    print(-1)
else:
    print(int(s[0]/(s[2]-s[1]))+1)
