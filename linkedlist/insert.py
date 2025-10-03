class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNewNodeAtTheFront(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node

    return head
    
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head = None
print("Empty List:")
print_list(head)

head = insertNewNodeAtTheFront(head, 30)
print("after inserting 30:")
print_list(head)


head = insertNewNodeAtTheFront(head, 40)
print("after inserting 40:")
print_list(head)

