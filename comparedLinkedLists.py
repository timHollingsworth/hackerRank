# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    if llist1 == None or llist2 == None:
        return 0
    n_1 = llist1 
    n_2 = llist2 
    while True:
        if not n_1 or not n_2:
            return 0
        elif n_1.data == n_2.data:
            if not n_1.next and not n_1.next:
                return 1
            else:
                n_1 = n_1.next 
                n_2 = n_2.next 
        else:
            return 0 
        
    