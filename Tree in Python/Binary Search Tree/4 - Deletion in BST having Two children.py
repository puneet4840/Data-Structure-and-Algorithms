# Delete the node having two children.
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def Insert_node(self,data):
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

    def Delete_Node(self):
        if self.root==None:
            print('\nTree is empty')
        else:
            ele=int(input("Enter the element having two childrens:  "))
            curr=self.root
            parent=curr
            while curr.data!=ele:
                parent=curr
                if ele>curr.data:
                    curr=curr.right
                else:
                    curr=curr.left
            if curr.left!=None and curr.right!=None:
                r=curr.right
                curr.data=r.data
                curr.right=None
                del r

    def Display(self):
        if self.root==None:
            print("\nTree is Empty")
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
        print('2: Delete Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            BST.Insert_node(item)
        elif ch==2:
            BST.Delete_Node()
        elif ch==3:
            BST.Display()
        elif ch==4:
            quit()
        elif ch==5:
            print('\nInvalid Choice')