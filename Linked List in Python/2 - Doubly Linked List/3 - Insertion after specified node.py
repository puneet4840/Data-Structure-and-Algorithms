# Insertion of node after a specified node in the linked list.
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Linked_List():
    def __init__(self):
        self.start=None

    def Insert_NOde(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            q=self.start
            while q.next!=None:
                q=q.next
            q.next=temp
            temp.prev=q
    
    def Insertion_After_Given_Node(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            ele=int(input("Enter the Element in the new node: "))
            new_node=Node(ele)
            pos=int(input("Enter the Data after to insert the node:  "))
            if pos==self.start:
                x=self.start.next
                self.start.next=new_node
                new_node.next=x
                new_node.prev=self.start
            else:
                ptr=self.start
                post_ptr=ptr.next
                while ptr.data!=pos:
                    ptr=ptr.next
                    post_ptr=ptr.next
                if ptr.next==None:
                    ptr.next=new_node
                    new_node.prev=ptr
                else:
                    ptr.next=new_node
                    new_node.next=post_ptr
                    new_node.prev=ptr

    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            x=self.start
            while x!=None:
                print(x.data,end='->')
                x=x.next

if __name__=="__main__":
    LL=Linked_List()
    print()
    while True:
        print('\n=============')
        print('1: Create Linked List')
        print('2: Insert Node after a given node:  ')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter your choice:  "))

        if ch==1:
            item=int(input("Enter the Elemenbt: "))
            LL.Insert_NOde(item)
        elif ch==2:
            LL.Insertion_After_Given_Node()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nLinked List is Empty')