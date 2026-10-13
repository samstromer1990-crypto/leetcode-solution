# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        def linked_list_to_list(data):
            result = []
            current = data
            while current is not None:
                result.append(current.val)  
                current = current.next
            return result 

        values = linked_list_to_list(head)
        
        unique_values = list(dict.fromkeys(values))
        
        if not unique_values:
            return None
            
        new_head = ListNode(unique_values[0])
        current = new_head
        for val in unique_values[1:]:
            current.next = ListNode(val)
            current = current.next
            
        return new_head