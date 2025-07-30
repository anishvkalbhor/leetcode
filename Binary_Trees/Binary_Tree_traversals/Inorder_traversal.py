# Initializing the Node/Root of the Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BinaryTreeTraversal(self, root):
    result = []

    def Inorder(node): # Left, Root, Right
        if node is None:
            return result
        
        Inorder(node.left)
        result.append(node.val)
        Inorder(node.right)

    Inorder(root)
    return result # [4, 2, 5, 1, 3]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
