# 1. odd_c =even_c
# 2. odd_c>even_c
n= int(input(""))
for i in range (0,n):
    e_c=0
    o_c=0
    l=int(input(""))
    ip=list(map(int,input().split(' ')))
    for j in range (0,l):
        if ip[j]%2==0:
            e_c+=1
        else:
            o_c+=1

    if e_c>=o_c :
        if o_c%2!=0:
            print(int(e_c))
        else:
            print(int(o_c/2))
    else:
        print(int(e_c))
        