N = int(input())
for i in range(0,N):
    turn = int(input())
    if turn <= 1 or (turn%7 == 0) or (turn%7 == 1):
        print("Second")
    else:
        print("First")
