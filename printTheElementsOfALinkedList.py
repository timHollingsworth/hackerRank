# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    currentNode = head
    while True:
        print(currentNode.data)
        if type(currentNode.next.data) == int:
            currentNode = currentNode.next 
        else:
            break