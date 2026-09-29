# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        
        def listnode_to_list(head):
            result = []
            current = head
            while current is not None:
                result.append(current.val)
                current = current.next
            return result   
        
        for head_node in lists:
            a.extend(listnode_to_list(head_node))
            
        output = sorted(a)
        
        dummy = ListNode(0)
        curr = dummy
        for val in output:
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next
        