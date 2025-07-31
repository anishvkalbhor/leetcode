class Node: # Binary Tree Node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution: # Solution Class
    def isBalanced(self, root):
        def check(root): # Helper Function to check if the tree is balanced using recursion
            if not root:
                return 0

            left = check(root.left) # Check the left subtree
            if left == -1:
                return -1

            right = check(root.right) # Check the right subtree
            if right == -1:
                return -1

            if abs(left - right) > 1: # If the difference between the left and right subtree is greater than 1, return -1
                return -1

            return 1 + max(left, right) # Return the height of the tree

        return check(root) != -1 # If the tree is balanced, return True, otherwise return False

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    print(sol.isBalanced(root))

