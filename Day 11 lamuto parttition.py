def lamutoPartition(a,l,h,p):
    a[p],a[h]=a[h],a[p]
    i=l-1
    pivot=a[h]
    for j in range(l,h):
        if a[j]<pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
a=[2,3,5,7,8,4,9]
lamutoPartition(a,0,6,5)
print(a)
