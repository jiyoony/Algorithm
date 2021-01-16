#문자열 반복
for i in range(int(input())):
    R=list(input())
    for j in range(2,len(R)):
        print(R[j]*int(R[0]),end='')
    print()
