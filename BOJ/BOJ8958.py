#ox퀴즈
#모르겠다
n=int(input())
for i in range(n):
    sco=input()
    count=0
    score=0
    for j in range(len(sco)):
        if sco[j] == 'O':
            count += 1
            score += count
        else:
            count=0
    print(score)
