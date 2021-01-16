#분해합
n=int(input())

def sum_digit(n):
    return sum([int(i) for i in str(n)])

for m in range(1,n):
    if (n==(m+sum_digit(m))):
        print(m)
        exit()
print(0)
