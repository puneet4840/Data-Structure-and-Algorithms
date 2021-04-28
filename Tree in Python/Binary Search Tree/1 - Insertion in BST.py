# Inserting the node in Binary Search Tree.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree():
    def __init__(self):
        self.root=None

    def Insert_Node(self,data):
        temp=Node(data)
        if self.root==None:
            self.root=temp
        else:
            curr=self.root
            parent=curr
            while curr!=None:
                parent=curr
                if temp.data>curr.data:
                    curr=curr.right
                elif temp.data<curr.data:
                    curr=curr.left
            if temp.data>parent.data:
                parent.right=temp
            else:
                parent.left=temp

    def Inorder(self,root):
        if root==None:
            print('\nTree is Empty')
        else:
            self.Inorder1(root)
            
    def Inorder1(self,root):
        if root==None:
            return
        else:
            self.Inorder1(root.left)
            print(root.data,end=' ')
            self.Inorder1(root.right)

if __name__ == '__main__':
    BST=Tree()
    print()
    while True:
        print('\n========')
        print('1: Insert Node')
        print('2: Display Inorder')
        print('3: Exit')
        ch=int(input("Enter your choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            BST.Insert_Node(item)
        elif ch==2:
            BST.Inorder(BST.root)
        elif ch==3:
            quit()
        else:
            print('\nInvalid Choice')