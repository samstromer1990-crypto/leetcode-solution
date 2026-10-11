# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        def linked_list_to_list(node):
            result = []
            current = node
            while current is not None:
                result.append(current.val)  
                current = current.next
            return result

        values = linked_list_to_list(head)
        
        output = []
        for i in values:
            if values.count(i) == 1:
                output.append(i)
            else:
                continue
                
        if not output:
            return None
            
        new_head = ListNode(output[0])
        current = new_head
        for val in output[1:]:
            current.next = ListNode(val)
            current = current.next
            
        return new_head