#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        i=0
        j=0
        l=[]
        while(i<n and j<m):
            if a[i]<b[j]:
                if i==0 or a[i-1]!=a[i]:
                    l.append(a[i])
                i=i+1
            elif a[i]>b[j]:
                if j==0 or b[j-1]!=b[j]:
                    l.append(b[j])
                j=j+1
            else:
                if i==0 or a[i-1]!=a[i]:
                    l.append(a[i])
                i=i+1
                j=j+1
        while(j<m):
            if j==0 or b[j-1]!=b[j]:
                l.append(b[j])
            j=j+1
        while(i<n):
            if i==0 or a[i-1]!=a[i]:
                l.append(a[i])
            i=i+1
        return l
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends
