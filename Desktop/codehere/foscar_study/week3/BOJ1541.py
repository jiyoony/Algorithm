#잃어버린 괄호
# n=str(input())
# result=0
# if '-' in n:
#     num=n.split('-')
#     result+=int(num[0])
#     for i in range(1,len(num)):
#         minus=num[i].split('+')
#         for k in range(len(minus)):
#             result-=int(minus[k])
#     print(result)
# else:
#     num=n.split('+')
#     for i in range(len(num)):
#         result+=int(num[i])
#     print(result)

#잃어버린 괄호
n=str(input())
result=0
if '-' in n:
    num=n.split('-')
    plus=num[0].split('+')
    plus=list(map(int,plus))
    result+=sum(plus)
    for i in range(1,len(num)):
        minus=num[i].split('+')
        minus=list(map(int,minus))
        result-=sum(minus)
    print(result)
else:
    num=n.split('+')
    num=list(map(int,num))
    print(sum(num))
