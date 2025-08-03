class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q): # Function to check if two binary trees are identical
        # If both nodes are None, they are identical
        if not q and not q:
            return True
        
        if not p or not q: # If one is None and the other is not, they are not identical
            return False
        
        return (p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)) # Check if the values of the nodes are equal and if the left and right subtrees are also identical
    
if __name__ == "__main__":
    # Example usage
    p = node(1)
    p.left = node(2)
    p.right = node(3)

    q = node(1)
    q.left = node(2)
    q.right = node(3)

    solution = Solution()
    print(solution.isSameTree(p, q))  # Output: True

    q.right.val = 4
    print(solution.isSameTree(p, q))  # Output: False

# Time Complexity: O(N+M) where N is the number of nodes in the first Binary Tree and M is the number of nodes in the second Binary Tree. This complexity arises from visiting each node of the two binary nodes during their comparison.

# Space Complexity: O(1) as no additional space or data structures is created that is proportional to the input size of the tree. O(H) Recursive Stack Auxiliary Space : The recursion stack space is determined by the maximum depth of the recursion, which is the height of the binary tree denoted as H. In the balanced case it is log2N and in the worst case (its N).