# Preorder Tree Traversal.
## It is a recursive approach to Preorder Tree Traversal.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def Preorder(self,root):
        if root==None:
            return
        else:
            print(root.data,end=' ')
            self.Preorder(root.left)
            self.Preorder(root.right)


if __name__ == '__main__':
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.left=Node(60)
    root.right.right=Node(70)

    T=Tree()
    print('\nPreorder\n')
    T.Preorder(root)