# Initializing the Node/Root of the Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BinaryTreeTraversal(self, root):
    result = []

    def Postorder(node): # Left, Right, Root
        if node is None:
            return result
        
        Postorder(node.left)
        Postorder(node.right)
        result.append(node.val)

    Postorder(root)
    return result # [4, 5, 2, 3, 1]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
