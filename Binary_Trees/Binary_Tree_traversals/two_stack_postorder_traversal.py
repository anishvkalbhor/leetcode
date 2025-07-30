class TreeNode: # Initializing the Node/Root of the Binary Tree
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # Two Stack Postorder Traversal
    def postorderTraversal(self, root):
        postOrder = [] # Initializing the postorder list
        
        if not root:
            return postOrder

        st1, st2 = [], [] # Initializing the two stacks

        st1.append(root) # Appending the root to the first stack

        while st1:
            root = st1.pop() # Popping the root from the first stack
            st2.append(root) # Appending the root to the second stack

            if root.left is not None:
                st1.append(root.left) # Appending the left child to the first stack

            if root.right is not None:
                st1.append(root.right) # Appending the right child to the first stack

        while st2:
            postOrder.append(st2[-1].val) # Appending the value of the root to the postorder list
            st2.pop() # Popping the root from the second stack

        return postOrder # [4, 5, 2, 3, 1]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().postorderTraversal(root))


# Time Complexity: O(n)
# Space Complexity: O(n)