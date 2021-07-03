#User function Template for python3

class Solution:
    #Function to return a list containing the intersection of two arrays.
    def printIntersection(self,a, b, n, m):
        l=[]
        i=0
        j=0
        while(i<n and j<m):
            if (i>0 and a[i-1]==a[i]):
                i=i+1
                continue
            if a[i]<b[j]:
                i=i+1
            elif a[i]>b[j]:
                j=j+1
            else:
                l.append(a[i])
                i=i+1
                j=j+1
        return l
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return: array of intersection of two array or -1
        '''
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        l = ob.printIntersection(a,b,n,m)
        print(*l)
# } Driver Code Ends
