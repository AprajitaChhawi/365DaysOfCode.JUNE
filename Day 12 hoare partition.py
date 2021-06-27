def HoarePartition(a,l,h,p):
    a[l],a[p]=a[p],a[l]
    pivot=a[l]
    i=l-1
    j=h+1
    while(True):
        i=i+1
        while(a[i]<=pivot):
            i=i+1
        j=j-1
        while(a[j]>pivot):
            j=j-1
        if(i>=j):
            return a
        a[i],a[j]=a[j],a[i]
    return a
a=[2,3,5,7,8,9,4]
a=HoarePartition(a,0,6,6)
print(a)
