# Postorder Tree Traversal.
## It is an recursive approach.

print()

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Tree():
    def Postorder(self,root):
        if root==None:
            return
        else:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.data,end=' ')


if __name__=="__main__":
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.right=Node(70)
    root.right.left=Node(60)

    T=Tree()
    print('\nPostorder\n')
    T.Postorder(root)