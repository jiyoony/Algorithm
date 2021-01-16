#알파벳 찾기
#모르겠어어어어
# s=list(map(str,input()))
# alphabet=list('abcdefghijklmnopqrstuvwxyz')
# for i in range(len(alphabet)):
#     print(s.find(alphabet[i]),map(alphabet))

print(*map(input().find,map(chr,range(97,123))),sep=' ')
