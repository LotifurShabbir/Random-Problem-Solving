class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Calculate the size of the linked list
        sz = 1
        temp = head
        while temp.next:
            sz += 1
            temp = temp.next
        
        k = k % sz
        
        if k == 0:
            return head
        
        
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        new_head = slow.next
        slow.next = None
        fast.next = head
        
        return new_head
