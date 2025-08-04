from collections import deque

class node: # Definition for a binary tree node.
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution: # Class to implement zigzag level order traversal of a binary tree.
    def zigzagTraversal(self, root): 

        result = [] # Initialize the result list to store the zigzag level order traversal.

        if not root: # If the root is None, return an empty list.
            return result
        
        nodesQueue = deque() # Use a deque to efficiently pop elements from both ends.
        nodesQueue.append(root) # Start with the root node in the queue.

        LeftToRight = True # A flag to determine the direction of traversal.

        while nodesQueue: # Continue until the queue is empty.

            size = len(nodesQueue)

            row = [0] * size # Initialize a row to store the current level's values.

            for i in range(size): # Traverse the current level.
                node = nodesQueue.popleft() # Pop the front node from the queue.

                index = i if LeftToRight else (size - 1 - i) # Determine the index based on the current direction.

                row[index] = node.val # Store the node's value in the row at the appropriate index.

                if node.left:
                    nodesQueue.append(node.left)
                if node.right:
                    nodesQueue.append(node.right)

            result.append(row) # Append the current row to the result.

            LeftToRight = not LeftToRight # Toggle the direction for the next level.

        return result # Return the zigzag level order traversal.
    
if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.left = node(6)
    root.right.right = node(7)

    solution = Solution()
    print(solution.zigzagTraversal(root))  # Output: [[1], [3, 2], [4, 5, 6, 7]]


# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(n), where n is the number of nodes in the binary tree (due to the queue storing nodes at each level).