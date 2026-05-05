class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        # Step 2: reduce k
        k = k % n
        if k == 0:
            return head
        
        # Step 3: make circular
        tail.next = head
        
        # Step 4: find new tail
        steps_to_new_tail = n - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Step 5: set new head
        new_head = new_tail.next
        
        # Step 6: break cycle
        new_tail.next = None
        
        return new_head