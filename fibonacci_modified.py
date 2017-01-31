"""
We define a modified Fibonacci sequence using the following definition:

Given terms  and  where , term  is computed using the following relation:
For example, if term  and , term , term , term , and so on.

Given three integers, , , and , compute and print term  of a modified Fibonacci sequence.

Note: The value of  may far exceed the range of a -bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to be more creative in your solution to compensate for the limitations of your chosen submission language.

Input Format

A single line of three space-separated integers describing the respective values of , , and .

Constraints

 may far exceed the range of a -bit integer.
Output Format

Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are  and .
"""

A,B,N = [int(x) for x in input().split(' ')]
if N==1:
    print(A)
if N==2:
    print(B)
else:
    for i in range(2,N):
        F=A + B*B
        A=B
        B=F
print(F)