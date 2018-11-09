#https://www.hackerrank.com/challenges/minimum-swaps-2/problem
def minimumSwaps(arr):
    c,i = 0,0
    while i < len(arr):
        if len(arr) == i:
            break
        if arr[i] == (i+1):
            i += 1
            continue 
        try:
            arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]
            c += 1
        except:
            break
    return c