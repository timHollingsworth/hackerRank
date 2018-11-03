# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    if head == None:
        return None 
    current_node = head 
    next_node = current_node.next 
    lst_data = [current_node.data]
    while next_node:
        current_node = next_node 
        next_node = current_node.next 
        lst_data.append(current_node.data)
    new_head = None 
    current_node = None
    for i in lst_data[::-1]:
        if new_head == None:
            new_head = SinglyLinkedListNode(i)
            current_node = new_head 
        else:
            current_node.next = SinglyLinkedListNode(i)
            current_node = current_node.next 
    return new_head