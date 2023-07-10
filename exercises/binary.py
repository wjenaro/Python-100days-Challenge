# Python program to find minimum depth of a given Binary Tree

# Tree node
class Node:
	def __init__(self , key):
		self.data = key
		self.left = None
		self.right = None

def minDepth(root):
	# Corner Case.Should never be hit unless the code is
	# called on root = NULL
	if root is None:
		return 0
	
	# Base Case : Leaf node.This accounts for height = 1
	if root.left is None and root.right is None:
		return 1
	
	# If left subtree is Null, recur for right subtree
	if root.left is None:
		return minDepth(root.right)+1
	
	# If right subtree is Null , recur for left subtree
	if root.right is None:
		return minDepth(root.left) +1
	
	return min(minDepth(root.left), minDepth(root.right))+1

# Driver Program
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)
root.right.left=Node(7)
root.right.right=Node(8)
root.left.left.left=Node(9)
print (minDepth(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)	
