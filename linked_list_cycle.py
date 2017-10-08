#https://www.hackerrank.com/challenges/ctci-linked-list-cycle
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    data_set = set()
    while head.next is not None:
    	if head.data in data_set:
    		return True
    	else:
    		data_set.add(head.data)
    		head.data=head.next.data
    return False
    
    
