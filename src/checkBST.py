#https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
#Made a mistake on this one by not reading (or knowing) the proper definition of BST.
#EVERY value of a node's left subtree must be less than the node's value.
#Made the mistake of checking only local values.
def checkBST(root):
	return check(root,0,10**4)
def check(node,min,max):
	if node is None:
		return True
	if node.data <= min or node.data >= max:
		return False
	return check(node.left,min,node.data) and check(node.right,node.data,max)

