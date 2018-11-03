# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if head == None:
        return None 
    elif position == 0:
        return head.next 
    else:
        current_node = head 
        next_node = head.next 
        for i in range(position-1):
            current_node = next_node 
            next_node = current_node.next 
        current_node.next = next_node.next 
        return head 