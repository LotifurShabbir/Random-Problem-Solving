# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []

        temp = head
        
        while temp != None:
            lst.append(temp.val)
            temp = temp.next

        l = 0
        r = k - 1
        for i in range(0, len(lst) // k):
            lst[l:r+1] = lst[l:r + 1][::-1]    
            l += k
            r += k
            
        result = ListNode(lst[0], None)
        tail  = result

        for i in range(1, len(lst)):
            n = ListNode(lst[i], None)
            tail.next = n
            tail = n
        return result