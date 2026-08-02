# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        input: head LL node
        output: reversed LL
        rules
        1. empty list return empty array

        prev = None
        next_node = 1


        curr = head
        prev = curr
                         p   
    None  <- 0<- 1<- 2<- 3  none
                             ^
                            nn



        Algo:
        1. prev = None
        2. NN = None
        3. curr = head
        4. while curr != None
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = = next_node

            return prev

        '''

        prev = None
        curr = head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
        