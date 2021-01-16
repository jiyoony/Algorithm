#단어의 개수
s=input().strip().split()
print(len(s))

'''
왜 이건 안되징??
s=input().strip()
a=s.split(' ')
print(len(a))


split(' ') 때문이었는데 왜지?????????????
공백 하나 입력했을 때도 리스트에 저장되어서 ??
split()과 split(' ')의 차이
'''






# a=list(s)
# count=0
# print(s)
# for i in range(len(s)):
#     if ord(a[i])==32:
#         count+=1
#         print(a[i])
# print(count+1)
