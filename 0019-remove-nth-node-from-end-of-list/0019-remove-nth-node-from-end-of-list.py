
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        
        vals.pop(-n)
        
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
            
        return dummy.next
        