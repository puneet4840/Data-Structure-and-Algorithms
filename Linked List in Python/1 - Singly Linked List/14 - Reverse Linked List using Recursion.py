# Reverse a Linked List Using Recursion.
print()

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.start=None
        
    def Insert_AT_END(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            p=self.start
            while p.next!=None:
                p=p.next
            p.next=temp

    def Reverse_LL(self,node):
        if (node==None) or (node.next==None):
            return node

        head=Reverse_LL(node.next)
        node.next.next=node
        node.next=None
        return head
        
    def Display(self):
        if self.start==None:
            print("\nLinked List is Empty")
        else:
            p=self.start
            while p!=None:
                print(p.data,end='->')
                p=p.next
            
if __name__ == "__main__":
    LL=Linked_list()
    print()
    while True:
        print('\n=============')
        print('1: Insert Node')
        print('2: Reverse the Linked List')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element:  "))
            LL.Insert_AT_END(item)
        elif ch==2:
            LL.Reverse_LL(LL.start)
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')   