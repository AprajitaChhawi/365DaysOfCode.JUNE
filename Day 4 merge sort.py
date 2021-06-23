#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        n1=m-l+1
        n2=r-m
        l1=[0]*n1
        l2=[0]*n2
        for i in range(n1):
            l1[i]=arr[l+i]
        for j in range(n2):
            l2[j]=arr[m+j+1]
        k=l
        i=0
        j=0
        while(i<n1 and j<n2):
            if l1[i]<=l2[j]:
                arr[k]=l1[i]
                i=i+1
                k=k+1
            else:
                arr[k]=l2[j]
                j=j+1
                k=k+1
        while(i<n1):
            arr[k]=l1[i]
            i=i+1
            k=k+1
        while(j<n2):
            arr[k]=l2[j]
            j=j+1
            k=k+1
        return arr
        # code here
    def mergeSort(self,arr, l, r):
        if l>=r:
            return 
        m=(r+l)//2
        ob=Solution()
        ob.mergeSort(arr,l,m)
        ob.mergeSort(arr,m+1,r)
        ob.merge(arr,l,m,r)
        return arr
        #code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
