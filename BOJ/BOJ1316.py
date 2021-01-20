#그룹단어체커
result=int(input())
for i in range(result):
    word=str(input())
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+2:]:
            result-=1
            break
print(result)

# flag
