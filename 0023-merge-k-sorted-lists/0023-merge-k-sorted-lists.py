# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        
        # 1. Helper to extract values from a linked list
        def listnode_to_list(head):
            result = []
            current = head
            while current is not None:
                result.append(current.val)
                current = current.next
            return result   
        
        # 2. Call the helper for EVERY linked list in 'lists'
        for head_node in lists:
            a.extend(listnode_to_list(head_node))
            
        # 3. Sort the extracted values
        output = sorted(a)
        
        # 4. Rebuild and return a linked list (ListNode), NOT a Python list
        dummy = ListNode(0)
        curr = dummy
        for val in output:
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next
        