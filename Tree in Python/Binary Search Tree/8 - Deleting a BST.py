# Delete BST.
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
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
                else:
                    curr=curr.left
            if temp.data>parent.data:
                parent.right=temp
            else:
                parent.left=temp

    def Delete_BST(self,root):
        if root==None:
            return root.data
        else:
            self.Delete_BST(root.left)
            self.Delete_BST(root.right)
            del root

    def Display(self):
        if self.root==None:
            print('\nTree is Empty')
        else:
            self.Inorder(self.root)

    def Inorder(self,root):
        if root==None:
            return
        else:
            self.Inorder(root.left)
            print(root.data,end=' ')
            self.Inorder(root.right)

    
if __name__=="__main__":
    BST=Tree()
    print()
    while True:
        print('\n===============')
        print('1: Insert Node')
        print('2: Delete Tree')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            BST.Insert_Node(item)
        elif ch==2:
            BST.Delete_BST(BST.root)
            print("\nTree is Deleted")
        elif ch==3:
            BST.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')