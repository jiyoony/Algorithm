#상수
# a,b=map(int,input().split())
# a_st=list(str(a))
# b_st=list(str(b))
# out1,out2="",""
# for i in range(0,3):
#     out1[i]+=a_st[3-(i+1)]
#     out2[i]+=b_st[3-(i+1)]
# print(out1)
# print(out2)


def swap(num):
    str_a = ""

    for i in range(3):
        str_a= str_a + str(num % 10)
        num = int(num / 10)
    return int(str_a)

a, b = map(int,input().split())

a = swap(a)
b = swap(b)

if a>b:
    print(a)
else:
    print(b)

    
