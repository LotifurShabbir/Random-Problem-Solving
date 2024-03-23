# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head == None or head.next == None:
            return head

        slow = head
        fast = head

        # finding middle
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        
        # counting length
        lenn = 0
        temp = head
        while temp != None:
            lenn += 1
            temp = temp.next
        # print(slow.val)
        if lenn % 2 == 0:
            # middle reverse
            revH = None
            temp = slow.next
            while temp != None:
                n = ListNode(temp.val, revH)
                revH = n
                temp = temp.next
            # print(revH)

            # modifing original list
            temp = head
            tail = temp
            
            while revH.next != None:
                temp = temp.next
                n = ListNode(revH.val)
                # print("n",n)
                tail.next = n
                tail = n
                revH = revH.next
                

                m = ListNode(temp.val)
                # print("m",m)
                tail.next = m
                tail = m
            tail.next = revH
            return head
        # print(slow.val)

        elif lenn % 2 != 0:
            middle_point = slow.val
            # print(middle_point)
            # middle reverse
            revH = None
            temp = slow.next
            while temp != None:
                n = ListNode(temp.val, revH)
                revH = n
                temp = temp.next
            # print(revH)

            # modifing original list
            temp = head
            tail = temp
            
            while revH.next != None:
                temp = temp.next
                n = ListNode(revH.val)
                # print("n",n)
                tail.next = n
                tail = n
                revH = revH.next
                

                m = ListNode(temp.val)
                # print("m",m)
                tail.next = m
                tail = m
                
            tail.next = revH
            tail = revH
            tail.next = ListNode(middle_point)
            return head