# Diameter of a Binary Tree is the longest path between any two nodes in the tree.
# The path may or may not pass through the root.
# The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
# The path may or may not pass through the root.

class Node: # Initializing the Node/Root of the Binary Tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution: # Diameter of the Binary Tree
    def diameter(self, root):
        self.max_diameter = 0 # Initializing the maximum diameter

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) # Recursively calling the left child
            right = dfs(node.right) # Recursively calling the right child
            self.max_diameter = max(self.max_diameter, left + right) # Updating the maximum diameter

            return 1 + max(left, right) # Returning the maximum height of the left and right child

        dfs(root) # Calling the dfs function
        return self.max_diameter # Returning the maximum diameter

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(Solution().diameter(root))

# Time Complexity: O(n^2)
# Space Complexity: O(1)

