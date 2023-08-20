'''
Maximum Subarray Sum https://cses.fi/problemset/task/1643

Input:
8
-1 3 -2 5 3 -5 2 2

Output:
9
'''

def maximumSubarraySum(n,arr):
    maxSum = 0

    for i in range(0, n):
        currSum = 0
        for j in range(i, n):
            currSum = currSum + arr[j]
            if(currSum > maxSum):
                maxSum = currSum

    return maxSum

n = int(input())
a = list(map(int, input().strip().split()))[:n]
print(maximumSubarraySum(n,a))