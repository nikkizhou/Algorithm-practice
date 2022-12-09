class Solution(object):
    def isValidBST(self, root):
        if root is None: return True
        if root.left is not None and root.val<self.maxVal(root.left):
            return False
        if root.right is not None and root.val>self.minVal(root.right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    
    def maxVal(self,root):
        while root.right is not None:
            root=root.right
        return root.val

    def minVal(self,root):
        while root.left is not None:
            root=root.left
        return root.val
