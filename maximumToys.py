#https://www.hackerrank.com/challenges/mark-and-toys/problem
# Complete the maximumToys function below.
def maximumToys(prices, k):
    count,sum = 0,0
    for i in sorted(prices):
        if sum <= k:
            sum+= i
            count+=1
    return count-1