#User function Template for python3

class Solution:
    '''
    The function should do the stated modifications in the given array arr[]
    Do not return anything.
    '''
    # arr[]: Input Array
    # N: Size of the Array arr[]
    #Function to segregate 0s, 1s and 2s in sorted increasing order.
    def segragate012(self,arr, N):
        low=0
        mid=0
        high=N-1
        while(mid<=high):
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low=low+1
                mid=mid+1
            elif arr[mid]==1:
                mid=mid+1
            else:
                arr[high],arr[mid]=arr[mid],arr[high]
                high=high-1
        return arr
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
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        ob=Solution()
        ob.segragate012(a,n)
        print(*a)
# } Driver Code Ends
