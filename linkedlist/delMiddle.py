class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return None
        slow, fast = head, head

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next= prev.next.next
        return head