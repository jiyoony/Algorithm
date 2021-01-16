#벌집
num=int(input())
plus=6
start=2
end=7
step=2
while True:
    if start<=num<=end:
        print(step)
        break

    elif num==1:
        print(1)
        break
    step+=1
    start+=plus
    plus+=6
    end+=plus
