# In Binary tree each node contains atmost 2 child nodes.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(50)
    root.left.right=Node(4)
    root.right.left=Node(5)
    root.right.right=Node(6)

    # print(root.data,end=' ')
    # print(root.left.data,end=' ')
    # print(root.right.data,end=' ')
    # print(root.left.left.data,end=' ')
    # print(root.left.right.data,end=' ')
    # print(root.right.left.data,end=' ')
    # print(root.right.right.data,end=' ')

    print('\t',root.data)
    print('   ',root.left.data,end='         ')
    print(root.right.data)
    print(' ',root.left.left.data,end='  ')
    print(root.left.right.data,end='     ')
    print(root.right.left.data,end='    ')
    print(root.right.right.data)
