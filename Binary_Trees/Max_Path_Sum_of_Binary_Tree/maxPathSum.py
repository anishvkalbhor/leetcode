class node: # Definition for a binary tree node.
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution: # Definition for a binary tree node.
    def maxPathSum(self, root):
        self.maxi = float('-inf') # Initialize maximum path sum to negative infinity

        def dfs(node): # Depth-first search to calculate maximum path sum
            if not node:
                return 0
            

            leftSum = max(0, dfs(node.left)) # Calculate maximum path sum from left subtree
            # If leftSum is negative, we consider it as 0 to not affect the maximum
            rightSum = max(0, dfs(node.right)) # Calculate maximum path sum from right subtree
            # If rightSum is negative, we consider it as 0 to not affect the maximum
            currentMax = node.val + leftSum + rightSum # Current maximum path sum including the current node
        
            self.maxi = max(self.maxi, currentMax) # Update the global maximum path sum
            return node.val + max(leftSum, rightSum) # Return the maximum path sum including the current node and one of its subtrees
        # Start DFS from the root node
    
        dfs(root)
        return self.maxi

if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

    solution = Solution()
    print(solution.maxPathSum(root))


# Time Complexity: O(n) where n is the number of nodes in the binary tree.
# Space Complexity: O(h) where h is the height of the binary tree due to recursion stack.