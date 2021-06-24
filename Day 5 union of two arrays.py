#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        i=0
        j=0
        count=0
        while(i<n and j<m):
            if (i>0 and (a[i] in a[:i])):
                i=i+1
                continue
            if (j>0 and (b[j] in b[:j])):
                j=j+1
                continue
            if (a[i]<b[j]) and (a[i] not in a[:i]):
                count=count+1
                i=i+1
            elif (a[i]>b[j]) and (b[j] not in b[:j]):
                count=count+1
                j=j+1
            else:
                count=count+1
                i=i+1
                j=j+1
        while(i<n and (a[i] not in a[:i])):
            count=count+1
            i=i+1
        while(j<m and (b[j] not in b[:j])):
            count=count+1
            j=j+1
        return count
                
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
