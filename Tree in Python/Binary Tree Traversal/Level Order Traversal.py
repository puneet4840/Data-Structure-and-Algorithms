# Level Order Traversal.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Tree():
    def Level_order(self,root):
        queue=list()
        queue.append(root)
        while len(queue)!=0:
            curr=queue[0]
            queue.pop(0)
            if curr.left!=None:
                queue.append(curr.left)
            if curr.right!=None:
                queue.append(curr.right)
            print(curr.data,end=' ')


if __name__=="__main__":
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.left=Node(60)
    root.right.right=Node(70)

    T=Tree()
    print('\nLevel Order Traversal\n')
    T.Level_order(root)