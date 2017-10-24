#https://www.hackerrank.com/challenges/ctci-linked-list-cycle
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

#Solution using a set
def has_cycle(head):
    data_set = set()
    while head.next is not None:
    	if head in data_set:
    		return True
    	else:
    		data_set.add(head)
    		head=head.next
    return False
    
#Solution using fast and slow pointer
def has_cycle2(head):
    if(head is None):
        return False
    slow = head
    fast = head.next
    while (slow != fast):
        if(fast is None or fast.next is None):
            return False
        slow = slow.next
        fast = fast.next.next
    return True
    
