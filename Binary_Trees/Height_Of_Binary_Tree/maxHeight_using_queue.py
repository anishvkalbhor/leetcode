from queue import Queue # Importing the Queue class


class Node: # Initializing the Node/Root of the Binary Tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution: # Maximum Height of the Binary Tree using Queue
    def maxHeight(self, root):
        if not root:
            return 0

        q = Queue() # Initializing the Queue
        level = 0 # Initializing the level
        q.put(root) # Putting the root in the Queue

        while not q.empty():
            size = q.qsize() # Getting the size of the Queue

            for i in range(size):
                front = q.get() # Getting the front element of the Queue

                if front.left is not None:
                    q.put(front.left) # Putting the left child in the Queue
                if front.right is not None:
                    q.put(front.right) # Putting the right child in the Queue
                
            level += 1 # Incrementing the level
        return level # Returning the level
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(Solution().maxHeight(root))

# Time Complexity: O(n)
# Space Complexity: O(n)