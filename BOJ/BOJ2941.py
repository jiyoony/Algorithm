#크로아티아 단어
n=input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for t in cro:
    n = n.replace(t,'*')
print(len(n))
