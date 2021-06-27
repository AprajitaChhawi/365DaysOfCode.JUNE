def NaivePartition(a,l,h,p):
    n=h-l+1
    temp=[0]*n
    index=0
    for i in range(l,h+1):
        if a[i]<=a[p]:
            temp[index]=a[i]
            index=index+1
    for i in range(l,h+1):
        if a[i]>a[p]:
            temp[index]=a[i]
            index=index+1
    for i in range(l,h+1):
        a[i]=temp[i]
a=[2,3,5,7,8,9,4]
NaivePartition(a,0,6,6)
print(a)
