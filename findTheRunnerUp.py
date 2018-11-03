"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up."""
if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    m = max(arr)
    runner_up = min(arr)
    for i in arr:
        if i < m and i > runner_up:
            runner_up = i
    print(runner_up)