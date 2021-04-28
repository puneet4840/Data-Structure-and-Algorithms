# Inorder Tree Traversal.
## It is recursive approach to traverse a tree in Inorder.

print()

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def Inorder(self,root):
        if root==None:
            return
        else:
            self.Inorder(root.left)
            print(root.data,end=' ')
            self.Inorder(root.right)


if __name__ == '__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)

    T=Tree()
    print('\nInorder Traversal\n')
    T.Inorder(root)