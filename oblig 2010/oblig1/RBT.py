RED = 'red'
BLACK = 'black'

class Tree:
	def __init__(self, root=None, nodes=set()):
		self.root = root
		self.nodes = nodes
		if root is not None:
			self.nodes.add(root)
      
	def insertNode(self, next_node, node):
		if node.key < next_node.key:
			if next_node.left is None:
				next_node.left = node
				node.parent = next_node
			else:
				self.insertNode(next_node.left, node)
			return
		if next_node.right is None:
			next_node.right = node
			node.parent = next_node
		else:
			self.insertNode(next_node.right, node)

	def addNode(self, node):
		self.nodes.add(node)
		self.insertNode(self.root, node)

class RedBlackTree(Tree):
	def __init__(self, root=None, nodes=set()):
		self.root = root
		self.nodes = nodes
		if root is not None:
			self.nodes.add(root)
			self.root.color = BLACK

	def insertNode(self, next_node, node):
		if node.key < next_node.key:
			if next_node.left.isLeaf():
				next_node.left = node
				node.parent = next_node
			else:
				self.insertNode(next_node.left, node)
			return
		if next_node.right.isLeaf():
			next_node.right = node
			node.parent = next_node
		else:
			self.insertNode(next_node.right, node)

	def rotateLeft(self, node):
		parent = node.parent
		right_child = node.right
		right_child_left = right_child.left

		parent.right = right_child
		right_child.parent = parent

		right_child.left = node
		node.parent = right_child

		node.right = right_child_left
		right_child_left.parent = node

		if node is self.root:
			self.root = right_child

	def rotateRight(self, node):
		parent = node.parent
		left_child = node.left
		left_child_right = left_child.right

		parent.left = left_child
		left_child.parent = parent

		left_child.left = node
		node.parent = left_child

		node.left = left_child_right
		left_child_right.parent = node

		if node is self.root:
			self.root = right_child


	def balance(self, node):
		if node is not self.root:
			if node.parent is None:
				return
      # case 1: parent is black, do nothing
			if node.parent.color is BLACK:
				return
			if node.getGrandparent() is not None:
				grandparent = node.getGrandparent()
				uncle = node.getUncle()
        # case 2:  both parent and uncle is red
				if uncle.color is RED:
					node.parent.color = BLACK
					uncle.color = BLACK
					grandparent.color = RED
					self.balance(grandparent)
					return
        # case 3: parent is red and uncle is black
        # case 3.1 LR unbalanced
				elif node is node.parent.right and node.parent is grandparent.left:
					self.rotateLeft(node.parent)
					node = node.left
        # case 3.2 RL unbalanced
				elif node is node.parent.left and node.parent is grandparent.right:
					self.rotateRight(node.parent)
					node = node.right
				grandparent = node.getGrandparent()
				node.parent.color = BLACK
				grandparent.color = RED
        # case 3.3 LL unbalanced
				if node is node.parent.left:
					self.rotateRight(grandparent)
        # case 3.4 RR unbalanced
				else:
					self.rotateLeft(grandparent)
		self.root.color = BLACK

	def addNode(self, node):
		self.nodes.add(node)
		self.insertNode(self.root, node)
		self.balance(node)

class Node():
	def __init__(self, key, parent=None, left=None, right=None):
		self.key = key
		self.parent = parent
		self.left = left
		self.right = right

	def getGrandparent(self):
		grandparent = None
		if self.parent is not None:
			grandparent = self.parent.parent
		return grandparent

	def getUncle(self):
		uncle = None
		if self.parent is not None and self.parent.parent is not None:
			if self.parent is self.getGrandparent().left:
				uncle = self.getGrandparent().right
			else:
				uncle = self.getGrandparent().left
		return uncle

class Leaf():
	def __init__(self, color=BLACK):
		self.key = None
		self.color = color

	def isLeaf(self):
		return True

class RedBlackNode(Node):
	def __init__(self, key, color=RED, parent=None, left=Leaf(), right=Leaf()):
		self.key = key
		self.parent = parent
		self.left = left
		self.right = right
		self.color = color

	def isLeaf(self):
		return False
		

node1 = RedBlackNode(13)
tree = RedBlackTree(node1)
values = [2, 15, 28, 5, 1, 30, 32]

for val in values:
	new_node = RedBlackNode(val)
	tree.addNode(new_node)
