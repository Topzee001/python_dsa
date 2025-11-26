class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def insertAtEnd(head, x):
    newNode = Node(x)

    if head is None:
        return newNode
    
    last = head

    while last.next is not None:
        last = last.next

    last.next = newNode

    return head
        

def printList(node):
    while node is not None:
        print(node.data, end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    
    print()

