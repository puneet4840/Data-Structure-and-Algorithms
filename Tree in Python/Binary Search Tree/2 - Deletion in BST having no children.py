# Deleting a given node in BST.
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
                else:
                    curr=curr.left
            if temp.data>parent.data:
                parent.right=temp
            else:
                parent.left=temp

    def Delete_leaf_node(self,ele):
        if self.root==None:
            print('\nTree is Empty')
        else:
            p=self.root
            upper=p
            while p.data!=ele:
                upper=p
                if ele>p.data:
                    p=p.right
                else:
                    p=p.left
            if upper.left==p:
                upper.left=None       
            else:
                upper.right=None

    def Inorder(self,root):
        if self.root==None:
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

if __name__ == "__main__":
    BST=Tree()
    print()
    while True:
        print('\n========')
        print('1: Insert Node')
        print('2: Delete given leaf node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            BST.Insert_Node(item)
        elif ch==2:
            ele=int(input("Enter the node to Delete: "))
            BST.Delete_leaf_node(ele)
        elif ch==3:
            BST.Inorder(BST.root)
        elif ch==4:
            quit()
        else:
            print('\nInvald Choice')
            