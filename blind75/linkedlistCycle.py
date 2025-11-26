# Definition for singly-linked list.
from typing import Optional
import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start = time.time()

        if head is None:
            return False
        # calculate start time
        h = head
        t = head
        while h and h.next is not None:
            h = h.next.next
            t = t.next
            if t == h:
                return True
        end = time.time()
        print(end - start)
        return False


# create helper function for the array and position for the head of the LL
def create_linked_list(arr, pos):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    cycle_node = None

    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

        if i == pos:
            cycle_node = curr

    # if pos == 0, cycle should start at head
    if pos == 0:
        cycle_node = head
    
    # create cycle if valid pos
    if pos!= -1:
        curr.next = cycle_node
    
    return head



sol = Solution()

head1 = create_linked_list([1,4,5,7,8], 1)
print("Has cycle? -> ", sol.hasCycle(head1))



