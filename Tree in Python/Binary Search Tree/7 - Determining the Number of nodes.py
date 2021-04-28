# Determining the number of nodes in the tree using recursion.
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
        self.count=0

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

    def No_of_Nodes(self,root):
        if root==None:
            return 0
        else:
            return self.No_of_Nodes(root.left)+self.No_of_Nodes(root.right)+1

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
        print('\n==============')
        print('1: Insert Node')
        print('2: Count Nodes')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            BST.Insert_Node(item)
        elif ch==2:
            n=BST.No_of_Nodes(BST.root)
            print(f'Total Number Of Nodes:  {n}')
        elif ch==3:
            BST.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')