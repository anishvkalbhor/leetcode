class Node: # Initializing the Node/Root of the Binary Tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution: # Maximum Height of the Binary Tree
    def maxHeight(self, root):
        if not root:
            return 0 # If the root is None, return 0

        left = self.maxHeight(root.left) # Recursively calling the left child
        right = self.maxHeight(root.right) # Recursively calling the right child

        return 1 + max(left, right) # Returning the maximum height of the left and right child

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)

    print(Solution().maxHeight(root))

# Time Complexity: O(n)
# Space Complexity: O(n)