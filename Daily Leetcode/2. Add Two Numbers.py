# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        second = ""
        
        i = l1
        while i != None:
            first += str(i.val)
            i = i.next
        # print(first)
        j = l2
        while j != None:
            second += str(j.val)
            j = j.next
        # print(second)

        first = first[::-1]
        second = second[::-1]
        # print(first, second)

        ans = int(first) + int(second)
        ans = str(ans)
        ans = ans[::-1]
        # print(ans)

        lst = []
        for i in ans:
            lst.append(int(i))
        # print(lst)

        head = ListNode(lst[0], None)
        tail = head

        for i in range(1, len(lst)):
            n = ListNode(lst[i], None)
            tail.next = n
            tail = n

        return head
        