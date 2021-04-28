# Delete Last Node
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
        
class Linked_List():
    def __init__(self):
        self.start=None
        
    def Insert_Node(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            q=self.start
            while q.next!=None:
                q=q.next
            q.next=temp
            temp.prev=q

    def Delete_Node(self):
        if self.start==None:
            print('\nLinked List is Empty')
        elif self.start.next==None:
            self.start=None
        else:
            z=self.start
            while z.next.next!=None:
                z=z.next
            z.next=None

    def Display(self):
        if self.start==None:
            print('\Linked List is Empty')
        else:
            p=self.start
            while p!=None:
                print(p.data,end='->')
                p=p.next

if __name__=="__main__":
    LL=Linked_List()
    print()
    while True:
        print('\n==========')
        print('1: Insert Node')
        print('2: Delete Last Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice:  "))

        if ch==1:
            item=int(input("Enter the Element: "))
            LL.Insert_Node(item)
        elif ch==2:
            LL.Delete_Node()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')