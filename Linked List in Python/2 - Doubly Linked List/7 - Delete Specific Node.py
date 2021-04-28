# Deleting specific node from the linked list.
print()

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
    
class Linked_List():
    def __init__(self):
        self.start=None

    def Insert_node(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp
        else:
            p=self.start
            while p.next!=None:
                p=p.next
            p.next=temp
            temp.prev=p

    def Delete_Specific(self):
        if self.start==None:
            print('\nLinked List is Empty')
        elif self.start.next==None:
            self.start=None
        else:
            ele=int(input("Enter the Element to delete node: "))
            if self.start.data==ele:
                self.start=self.start.next
            else:
                ptr=self.start
                pre_ptr=None
                while ptr.data!=ele:
                    pre_ptr=ptr
                    ptr=ptr.next
                if ptr.next==None:
                    pre_ptr.next=None
                else:
                    ptr.next.prev=pre_ptr
                    pre_ptr.next=ptr.next
                
    def Display(self):
        if self.start==None:
            print('\nLinked List is Empty')
        else:
            z=self.start
            while z!=None:
                print(z.data,end='->')
                z=z.next
                

if __name__ == "__main__":
    LL=Linked_List()
    print()
    while True:
        print('\n===========')
        print('1: Insert Node')
        print('2: Delete Specific Node')
        print('3: Display')
        print('4: Exit')
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            item=int(input("Enter the Element: "))
            LL.Insert_node(item)
        elif ch==2:
            LL.Delete_Specific()
        elif ch==3:
            LL.Display()
        elif ch==4:
            quit()
        else:
            print('\nInvalid Choice')