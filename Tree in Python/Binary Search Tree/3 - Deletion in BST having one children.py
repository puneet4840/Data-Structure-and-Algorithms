# Deletion in BST having one children.
print()

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Linked_list:
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

    def Delete_Node(self,ele):
        if self.root==None:
            print("\nTree is Empty")
        else:
            ptr=self.root
            parent=ptr
            while ptr.data!=ele:
                parent=ptr
                if ele>ptr.data:
                    ptr=ptr.right
                else:
                    ptr=ptr.left
            if ptr==parent.right:
                if ptr.right!=None:
                    parent.right=ptr.right
                else:
                    parent.right=ptr.left
            else:
                if ptr.right!=None:
                    parent.left=ptr.right
                else:
                    parent.left=ptr.left

    def Display(self):
        if self.root==None:
            print('\nTree is Empty')
        else:
            self.Inorder1(self.root)

    def Inorder1(self,root):
        if root==None:
            return
        else:
            self.Inorder1(root.left)
            print(root.data,end=' ')
            self.Inorder1(root.right)

if __name__=="__main__":
    BST=Linked_list()
    print()
    while True:
        print('\n============')
        print('1: Insert Node')
        print('2: Delete Node Having One Child')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            BST.Insert_node(item)
        elif ch==2:
            ele=int(input("Enter the Element which has only one child node:  "))
            BST.Delete_Node(ele)
        elif ch==3:
            BST.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')