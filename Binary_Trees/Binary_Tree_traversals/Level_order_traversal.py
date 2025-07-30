from collections import deque


class Node: # Initializing the Node/Root of the Binary Tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeTraversal: # Level Order Traversal
    def LevelOrder(self, root):

        ans = [] # Initializing the answer list
        if root is None:
            return ans
        
        queue = deque() # Initializing the queue
        queue.append(root)

        while queue:
            size = len(queue) # Getting the size of the queue
            level = [] # Initializing the level list

            for i in range(size):
                node = queue.popleft() # Getting the node from the queue
                level.append(node.val) # Appending the node value to the level list

                if node.left:
                    queue.append(node.left) # Appending the left child to the queue
                if node.right:
                    queue.append(node.right) # Appending the right child to the queue

            ans.append(level) # Appending the level list to the answer list
        return ans # [[1], [2, 3], [4, 5]]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(BinaryTreeTraversal().LevelOrder(root))