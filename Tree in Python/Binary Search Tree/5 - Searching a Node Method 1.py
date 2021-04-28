# Searching a node in Binry Search Tree.
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
            ptr=self.root
            parent=ptr
            while ptr!=None:
                parent=ptr
                if temp.data>ptr.data:
                    ptr=ptr.right
                else:
                    ptr=ptr.left
            if temp.data>parent.data:
                parent.right=temp
            else:
                parent.left=temp
    
    def Search_Node(self,ele):
        if self.root==None:
            print('\nTree is Empty')
        else:
            curr=self.root
            parent=curr
            while curr.data!=ele:
                parent=curr
                if ele>curr.data:
                    curr=curr.right
                else:
                    curr=curr.left
            if curr==None:
                print('\nGiven Element is not present in the Tree.')
            else:
                if curr==parent.right:
                    print(f'\n{ele} is found at right side of {parent.data} element.')
                else:
                    print(f'\n{ele} is found at left side of {parent.data} element.')

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
        print('2: Search Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            BST.Insert_Node(item)
        elif ch==2:
            ele=int(input("Enter the Element to Search: "))
            BST.Search_Node(ele)
        elif ch==3:
            BST.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')