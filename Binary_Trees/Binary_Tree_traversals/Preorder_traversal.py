# Initializing the Node/Root of the Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BinaryTreeTraversal(self, root):
    result = []

    def Preorder(node): # Root, Left, Right
        if node is None:
            return result
        
        result.append(node.val)
        Preorder(node.left)
        Preorder(node.right)

    Preorder(root)
    return result # [1, 2, 4, 5, 3]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
