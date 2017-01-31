"""
Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters  and  only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format

The first line contains an integer , i.e. the number of test cases. 
The next  lines contain a string each.

Output Format

For each test case, print the minimum number of deletions required.
"""
N = int(input())
for i in range(N):
    S = list(input().strip())
    prev=''
    D = 0
    for L in S:
        if L == prev:
            D += 1
        prev = L
    print(D)