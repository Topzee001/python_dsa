# Traversal of Singly Linked List is one of the fundamental operations,
# where we traverse or visit each node of the linked list
# iterative approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseList(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

traverseList(head)