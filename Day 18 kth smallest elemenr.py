#User function Template for python3

class Solution:
    #Function to find the kth smallest element in the array.
    def kthSmallest(self,a,n,k):
        low=0
        high=n-1
        while(low<=high):
            p=self.partition(a,low,high)
            if p==k-1:
                return a[p]
            elif p>k-1:
                high=p-1
            else:
                low=p+1
    def partition(self,a,low,high):
        pivot=a[high]
        i=low-1
        for j in range(low,high):
            if a[j]<pivot:
                i=i+1
                a[i],a[j]=a[j],a[i]
        a[i+1],a[high]=a[high],a[i+1]
        return i+1
            
       
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k= map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.kthSmallest(a,n,k))
# } Driver Code Ends
