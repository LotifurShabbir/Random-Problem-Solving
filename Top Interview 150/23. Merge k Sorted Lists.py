# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i in range(len(lists)):
            temp = lists[i]
            while temp != None:
                lst.append(temp.val)
                temp = temp.next
        lst.sort()
        if len(lst) < 1:
            return
        res = ListNode(lst[0], None)
        tail = res

        for i in range(1, len(lst)):
            n  = ListNode(lst[i], None)
            tail.next = n
            tail = n
        return res
        
        