class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def countandmerge(self,arr,l,m,r):
        n1=m-l+1
        n2=r-m
        l1=[0]*n1
        l2=[0]*n2
        for i in range(n1):
            l1[i]=arr[l+i]
        for i in range(n2):
            l2[i]=arr[m+i+1]
        k=l
        i=0
        j=0
        r=0
        while(i<n1 and j<n2):
            if l1[i]<=l2[j]:
                arr[k]=l1[i]
                i=i+1
            else:
                arr[k]=l2[j]
                r=r+(n1-i)
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
        return r
    def countInversion(self,arr,l,r):
        re=0
        if(l<r):
            m=(l+r)//2
            re=re+self.countInversion(arr,l,m)
            re=re+self.countInversion(arr,m+1,r)
            re=re+self.countandmerge(arr,l,m,r)
        return re
    def inversionCount(self, arr, n):
        res=self.countInversion(arr,0,n-1)
        return res
        # Your Code Here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
