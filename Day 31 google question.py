def google(l,a):
    s=l[0]
    for i in range(1,len(l)):
        s=s&l[i]
    print(s)
    return s&a==1
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    while k:
        k=k-1
        a=int(input())
        if (google(l,a)):
            print('Yes')
        else:
            print('No')
    
