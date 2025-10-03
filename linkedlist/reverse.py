class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    prev, curr = None, head

    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    print(prev)
    return prev

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Reverse and get the new head
new_head = reverseList(head)

# Print the reversed list to verify
current = new_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")