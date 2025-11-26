# Definition for singly-linked list.
from typing import Optional
import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # calculate start time
        h = head
        t = head
        while h and h.next is not None:
            h = h.next.next
            t = t.next
            if t == h:
                return True
        return False

