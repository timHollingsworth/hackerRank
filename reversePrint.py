# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    if head == None:
        return None 
    current_node = head 
    next_node = current_node.next 
    lst_data = [current_node.data]
    while next_node:
        current_node = next_node 
        next_node = current_node.next
        lst_data.append(current_node.data)
    for i in lst_data[::-1]:
        print(i)